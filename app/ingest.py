import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


VECTOR_PATH = "data/vectorstore"


def ingest(file_path):

    print("Step 1: Loading document...")

    if not os.path.exists(file_path):
        print("File not found")
        return

    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    print("Step 2: Splitting document...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print("Number of chunks:", len(chunks))

    print("Step 3: Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Step 4: Creating vector store...")

    # THIS MUST BE INSIDE THE FUNCTION
    if os.path.exists(VECTOR_PATH):

        vectorstore = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        vectorstore.add_documents(chunks)

    else:

        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

    vectorstore.save_local(VECTOR_PATH)

    print("Ingestion complete")
