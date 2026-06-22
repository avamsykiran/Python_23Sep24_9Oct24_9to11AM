from __future__ import annotations

# pip install langchain langchain-community langchain-text-splitters langchain-ollama chromadb pypdf sentence-transformers

import argparse
from pathlib import Path

# Modern RAG orchestration modules
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# Correct component namespace locations
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama

def load_bye_law_documents(pdf_path: Path):
    if not pdf_path.exists():
        raise FileNotFoundError(f"Bye-law PDF not found: {pdf_path}")

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=150)
    return splitter.split_documents(documents)


def create_vectorstore(documents, persist_directory: Path):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma.from_documents(
        documents=documents, 
        embedding=embeddings, 
        persist_directory=str(persist_directory)
    )

def get_retriever(persist_directory: Path, pdf_path: Path, rebuild: bool = False):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    if rebuild or not persist_directory.exists() or not any(persist_directory.iterdir()):
        documents = load_bye_law_documents(pdf_path)
        persist_directory.mkdir(parents=True, exist_ok=True)
        vectorstore = create_vectorstore(documents, persist_directory)
    else:
        vectorstore = Chroma(
            persist_directory=str(persist_directory), 
            embedding_function=embeddings
        )

    return vectorstore.as_retriever(search_kwargs={"k": 4})

def format_docs(docs):
    """Helper function to combine retrieved document chunks into a single text block."""
    return "\n\n".join(doc.page_content for doc in docs)

def build_qa_chain(retriever):
    llm = ChatOllama(model="llama3", temperature=0.3)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant specialized in legal and community bye-laws. "
                   "Answer the question based strictly on the provided context down below. "
                   "If you do not know the answer, state that it is not covered in the document.\n\n"
                   "Context:\n{context}"),
        ("human", "{input}"),
    ])
    
    # This pure LCEL pipe creates a clean, future-proof RAG pipeline
    modern_rag_chain = (
        {
            "context": retriever | format_docs, 
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return modern_rag_chain

def run_query(chain, query: str):
    # Sends the query string directly through the pipe execution layers
    answer = chain.invoke(query)    
   
    return answer

def display_menu():
    print("\n=== MVV City Bye Laws RAG Assistant ===")
    print("1. Ask a question")
    print("2. Rebuild vector store from PDF")
    print("3. Show vector store status")
    print("4. Exit")

def show_status(persist_directory: Path):
    if not persist_directory.exists():
        print("Vector store is not created yet.")
        return
    files = list(persist_directory.glob("**/*"))
    print(f"Vector store path: {persist_directory}")
    print(f"Persisted files: {len(files)}")
    if files:
        for file in files[:10]:
            print(f"  - {file.name}")
        if len(files) > 10:
            print("  ...")


def interactive_menu(qa_chain, persist_dir: Path, pdf_path: Path):
    current_chain = qa_chain
    while True:
        display_menu()
        choice = input("Select an option [1-4]: ").strip()
        if choice == "1":
            query = input("\nEnter your question: ").strip()
            if not query:
                print("Please enter a valid question.")
                continue
            answer = run_query(current_chain, query)
            print("\n=== Answer ===")
            print(answer)            
        elif choice == "2":
            print("\nRebuilding vector store from PDF... this may take a moment.")
            retriever = get_retriever(persist_dir, pdf_path, rebuild=True)
            current_chain = build_qa_chain(retriever)
            print("Rebuild complete.")
        elif choice == "3":
            show_status(persist_dir)
        elif choice == "4":
            print("Exiting. Thank you for using the RAG assistant.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


def main():
    parser = argparse.ArgumentParser(
        description="Local RAG assistant for MVV City Bye Laws using Ollama llama3."
    )
    parser.add_argument("--query", "-q", help="Question to ask about the bye-law document.")
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Rebuild the local vector store from the PDF.",
    )
    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent
    pdf_path = base_dir / "MVV CITY BYE LAWS.pdf"
    persist_dir = base_dir / "bye_laws_chroma"

    retriever = get_retriever(persist_dir, pdf_path, rebuild=args.rebuild)
    qa_chain = build_qa_chain(retriever)

    if args.query:
        answer = run_query(qa_chain, args.query)
        print("\n=== Answer ===")
        print(answer)        
        return

    print("Welcome to the MVV City Bye Laws RAG assistant.")
    print("Make sure Ollama is running locally with the llama3 model.")
    interactive_menu(qa_chain, persist_dir, pdf_path)


if __name__ == "__main__":
    main()