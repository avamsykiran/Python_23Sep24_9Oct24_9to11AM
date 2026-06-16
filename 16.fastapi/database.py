from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session

# SQLite database URL
DATABASE_URL = "sqlite:///./items.db"

# Create database engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models (SQLModel base)
Base = SQLModel

# Create all tables
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency function to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============== OLD CODE (COMMENTED OUT) ==============
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# # SQLite database URL
# DATABASE_URL = "sqlite:///./items.db"
#
# # Create database engine
# engine = create_engine(
#     DATABASE_URL, 
#     connect_args={"check_same_thread": False}
# )
#
# # Create session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # Create base class for models
# Base = declarative_base()
#
# # Dependency function to get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# ======================================================
