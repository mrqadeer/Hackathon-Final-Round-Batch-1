import os
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

# Custom modules for help
from utils.get_qa_chain import QAChain
from utils.helpers import get_collections_names
from utils.helpers import copy_to_project_folder
from utils.get_texts import get_text_chunks_recursive, get_vectorstore, get_docx_text, get_pdf_text
from utils.helpers import custom_files_loader
qa=QAChain() # object of my custom mudoul class for use in file
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def chatbot():
    """
    This function is main function that runs the chatbot
    :return: It returns question and answer
    """
    # Setting up header
    st.subheader("Welcome to ChatBot")

    # Initialization of states
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "processComplete" not in st.session_state:
        st.session_state.processComplete = None
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = None

    # Expander block
    with st.expander("Documents"):
        col1, col2 = st.columns([3, 2])  # 2 columns side by side

        with col1:
            uploaded_files = st.file_uploader("Upload your file", 
                    type=['pdf', "docx"], accept_multiple_files=True)
            process = st.button("Process", key="process")
            if process and len(uploaded_files)>0:
                # Function that copy uploaded files into directory "data-files"
                copy_to_project_folder(uploaded_files)

                # Empty list for chunks
                text_chunks_list = []

                # Processing
                with st.spinner("Processing files"):
                    for file in uploaded_files:
                        if file.name.endswith(".pdf"):
                            file_name = file.name  # name of file
                            pdf_file = f"data-files/{file_name}"  # Path of file to be loaded

                            # Reading file from function defined
                            text = get_pdf_text(pdf_file)

                        elif file.name.endswith(".docx"):
                            file_name = file.name
                            file = f"data-files/{file_name}"
                            # Reading docx file
                            text = get_docx_text(file)

                        # get text chunks
                        text_chunks = get_text_chunks_recursive(text)  # take text from above methods and return chunks
                        text_chunks_list.extend(text_chunks)

                    # taking random collection name
                    collection_name = get_collections_names()

                    # create vector stores
                    vectorstore = get_vectorstore(text_chunks_list, collection_name)

                no_of_chunks = len(text_chunks_list)

                # create conversation chain
                st.session_state.conversation = qa.get_qa_chain(vectorstore, no_of_chunks)
                st.session_state.processComplete = True
            else:
                st.warning("Please upload files")
                # st.stop()

        # Section for loading zipped files
        with col2:
            st.write("Keep your zipped files in a directory and press button given below.")
            setup = st.button("Process", key="setup")

            if setup:
                custom_files_loader("data-files/zipped.zip")
                text_chunks_list = []

                # Process the stuff
                with st.spinner("Processing files"):
                    for file in os.listdir("data-files"):
                        if file.endswith(".pdf"):
                            file_name = file
                            pdf_file = f"data-files/{file_name}"
                            text = get_pdf_text(pdf_file)

                        elif file.endswith(".docx"):
                            file_name = file
                            st.write(file_name)

                            file = f"data-files/{file_name}"
                            text = get_docx_text(file)

                        # get text chunks
                        text_chunks = get_text_chunks_recursive(text)
                        text_chunks_list.extend(text_chunks)
                    # getting collection name
                    collection_name = get_collections_names()
                    # create vector stores
                    vectorstore = get_vectorstore(text_chunks_list, collection_name)

                # create conversation chain
                no_of_chunks = len(text_chunks_list)
                st.session_state.conversation = qa.get_qa_chain(vectorstore, no_of_chunks)  

                st.session_state.processComplete = True

    if st.session_state.processComplete:
        user_question = st.chat_input("Ask Question about your files.")
        if user_question:
            handel_userinput(user_question)


def handel_userinput(user_question):
    """

    :param user_question: This function for responsible for handling user input from the user and sending it to the use
    :return: It is chat interface
    """
    with st.spinner('Generating response...'):
        result = st.session_state.conversation({"query": user_question})
        response = result['result']
        source = result['source_documents'][0].metadata['source']
    st.session_state.chat_history.append(user_question)
    st.session_state.chat_history.append(
        f"{response} \n Source Document: {source}")

    # Layout of input/response containers
    response_container = st.container()

    with response_container:
        for i, messages in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                message(messages, is_user=True, key=str(i),
                        avatar_style="adventurer-neutral")
            else:
                message(messages, key=str(i))


if __name__ == '__main__':
    chatbot()
