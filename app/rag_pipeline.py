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
    embedding_model = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents,
        embedding_model
    )

    return vectorstore


def load_vector_store():
    """
    Load saved FAISS vector DB
    """
    embedding_model = get_embedding_model()

    vectorstore = FAISS.load_local(
        "vectorstore",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def retrieve_chunks(query: str):
    """
    Retrieve relevant chunks based on user query
    """
    vectorstore = load_vector_store()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}  
    )

    docs = retriever.invoke(query)

    return docs