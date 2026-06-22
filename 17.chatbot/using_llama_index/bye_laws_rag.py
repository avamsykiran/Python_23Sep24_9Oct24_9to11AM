from __future__ import annotations

# pip install llama-index llama-index-llms-ollama llama-index-embeddings-huggingface pypdf

import argparse
from pathlib import Path

from llama_index.core import (
    Settings,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.schema import Document
from pypdf import PdfReader

# Model integration wrappers
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def configure_global_settings():
    """Configures dependency injection components across the global LlamaIndex instance."""
    # 1. Initialize local LLM via Ollama
    Settings.llm = Ollama(model="llama3", request_timeout=60.0, temperature=0.3)
    
    # 2. Set up local embedding engine matching the sentence-transformer schema
    Settings.embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")
    
    # 3. Configure chunk parsing strategy (Token length equivalent to Character Splitter)
    Settings.node_parser = TokenTextSplitter(chunk_size=300, chunk_overlap=40)


def load_pdf_documents(pdf_path: Path) -> list[Document]:
    """Load and convert each PDF page into a Document with metadata."""
    reader = PdfReader(str(pdf_path))
    documents: list[Document] = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if not text.strip():
            continue
        metadata = {
            "file_name": pdf_path.name,
            "file_path": str(pdf_path),
            "page_label": page_number,
        }
        documents.append(Document(text=text, metadata=metadata))

    if not documents:
        raise RuntimeError(
            f"Failed to extract any text from PDF: {pdf_path}. "
            "Please verify the file is text-searchable."
        )
    return documents


def get_query_engine(persist_directory: Path, pdf_path: Path, rebuild: bool = False):
    """Retrieves or builds the Vector Storage Index and compiles a high-level Query Engine."""
    configure_global_settings()

    if rebuild or not persist_directory.exists() or not any(persist_directory.iterdir()):
        if not pdf_path.exists():
            raise FileNotFoundError(f"Bye-law PDF not found: {pdf_path}")
        
        print("\n[Parsing] Extracting PDF text and building local vector index...")
        documents = load_pdf_documents(pdf_path)
        
        # Build vector store layout and persist straight to storage path
        index = VectorStoreIndex.from_documents(documents)
        persist_directory.mkdir(parents=True, exist_ok=True)
        index.storage_context.persist(persist_dir=str(persist_directory))
    else:
        # Fast disk-load step for pre-cached indices
        storage_context = StorageContext.from_defaults(persist_dir=str(persist_directory))
        index = load_index_from_storage(storage_context)

    # Convert the vector store index directly into a conversational stateless query wrapper
    return index.as_query_engine(
        similarity_top_k=4,
        system_prompt=(
            "You are a helpful assistant specialized in legal and community bye-laws. "
            "Answer the question based strictly on the provided context down below. "
            "If you do not know the answer, state that it is not covered in the document."
        )
    )


def run_query(query_engine, query: str):
    """Executes a text retrieval query and strips out matching context payloads."""
    # The LlamaIndex runtime returns an intelligent Response object
    response_obj = query_engine.query(query)
    
    answer = str(response_obj)
    # LlamaIndex registers matching chunks as NodeWithScore objects inside 'source_nodes'
    sources = response_obj.source_nodes
    return answer, sources


def print_sources(sources):
    if not sources:
        print("No source documents were retrieved.")
        return

    print("\n--- Retrieved Source Chunks ---")
    for index, node_with_score in enumerate(sources, start=1):
        node = node_with_score.node
        score = node_with_score.score
        
        # Pull tracking variables safely directly from metadata injection keys
        source_file = node.metadata.get("file_name", "Unknown File")
        page_num = node.metadata.get("page_label", "Unknown Page")
        preview = node.text.strip().replace("\n", " ")[:400]
        
        print(f"[{index}] file={source_file} (Page {page_num}) | Confidence Match: {score:.4f}")
        print(f"    {preview}\n")
    print("---")


def display_menu():
    print("\n=== MVV City Bye Laws RAG Assistant (LlamaIndex) ===")
    print("1. Ask a question")
    print("2. Rebuild vector store from PDF")
    print("3. Show vector store status")
    print("4. Exit")


def show_status(persist_directory: Path):
    if not persist_directory.exists():
        print("Vector store storage folder does not exist yet.")
        return
    files = list(persist_directory.glob("*"))
    print(f"Vector store path: {persist_directory}")
    print(f"Persisted storage components: {len(files)}")
    if files:
        for file in files:
            print(f"  - {file.name}")


def interactive_menu(query_engine, persist_dir: Path, pdf_path: Path):
    current_engine = query_engine
    while True:
        display_menu()
        choice = input("Select an option [1-4]: ").strip()
        if choice == "1":
            query = input("\nEnter your question: ").strip()
            if not query:
                print("Please enter a valid question.")
                continue
            answer, sources = run_query(current_engine, query)
            print("\n=== Answer ===")
            print(answer)
            print_sources(sources)
        elif choice == "2":
            print("\nRebuilding vector store from PDF... this may take a moment.")
            current_engine = get_query_engine(persist_dir, pdf_path, rebuild=True)
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
        description="Local RAG assistant for MVV City Bye Laws using LlamaIndex and Ollama."
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
    persist_dir = base_dir / "bye_laws_llamaindex"

    query_engine = get_query_engine(persist_dir, pdf_path, rebuild=args.rebuild)

    if args.query:
        answer, sources = run_query(query_engine, args.query)
        print("\n=== Answer ===")
        print(answer)
        print_sources(sources)
        return

    print("Welcome to the MVV City Bye Laws RAG assistant.")
    print("Make sure Ollama is running locally with the llama3 model.")
    interactive_menu(query_engine, persist_dir, pdf_path)


if __name__ == "__main__":
    main()