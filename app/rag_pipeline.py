

from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str):
    """
    Convert raw text into chunked Document objects
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    documents = text_splitter.create_documents([text])

    return documents