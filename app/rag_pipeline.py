from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from app.embeddings import get_embedding_model


def chunk_text(text: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    documents = text_splitter.create_documents([text])
    return documents


def create_vector_store(documents):
    """
    Convert chunks into embeddings and store in FAISS
    """
    embedding_model = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents,
        embedding_model
    )

    return vectorstore