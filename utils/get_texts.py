import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings

# set up credentials
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")


# Function to read PDF Files
def get_pdf_text(pdf):
    """
    :param pdf:This function take  pdf file as input
    :return: It returns the text document
    """

    pdf_reader = PyPDFLoader(pdf)  # loading object
    loader = pdf_reader.load()
    return loader


def get_docx_text(file):
    """
    :param file:This function take  MS Word file path
    :return: It returns the text document
    """
    loader = Docx2txtLoader(file)
    text = loader.load()
    return text


def get_text_chunks_recursive(docs):
    """
    :param docs: This function takes a list of documents for splitting
    :return: It returns the chunks of documents
    """

    # Splitting the text
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "."],
        chunk_size=900,
        chunk_overlap=100,
        length_function=len
    )

    # Making chunks
    chunks = text_splitter.split_documents(docs)

    return chunks


def get_vectorstore(text_chunks, collection_name):
    """

    :param text_chunks: This function takes chunks of text
    :param collection_name: A unique name for the collection of vectors
    :return:
    """

    try:
        # creating the Vector Store using HuggingFace Model
        embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        # embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-large-v2")

        # Making knowledge base
        knowledge_base = Qdrant.from_documents(
            documents=text_chunks,
            embedding=embeddings,
            url=qdrant_url,
            prefer_grpc=True,
            api_key=qdrant_api_key,
            collection_name=collection_name,
        )
    except Exception as e:
        st.write(f"Error: {e}")
    else:
        return knowledge_base
