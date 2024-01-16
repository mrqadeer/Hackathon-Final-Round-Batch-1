import streamlit as st
from streamlit_option_menu import option_menu
# Custom modules
from utils.chatbot import chatbot

# Setting up Page
st.set_page_config(page_title="Chatbot", page_icon="💬")


class MyApp:
    # Constructor of class
    def __init__(self):
        st.title("Chat with Documents")
        self.apps = []
        st.markdown("---")

    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})


    def run(self):
        """
        This method run the streamlit app
        """
        with st.sidebar:
            app = option_menu(
                menu_title='Chat Zone',
                options=['Home', 'PDF'],
                icons=['house-heart', 'file-pdf-fill'],
                menu_icon='chat-text-fill',
                default_index=0,

                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "magenta"},
                    "nav-link-selected": {"background-color": "#02ab21"}, })
        if app == "PDF":
            chatbot()
        if app=="Home":

            data = ['Sir Irfan Malik',"Xeven Solutions", 'Hope To Skill',
                    'Artificial Intelligence Course Batch 1',"Hackathon Final Round"]
            for name in data:
                st.subheader(name, divider='rainbow')
            # st.header("")
            # st.subheader("")
            with st.expander("About the chatbot"):
                st.markdown("""This chatbot allows you to chat with your documents like MS Word files and PDF 
                files.This chatbot is designed in way that it can retrieve documents from.""")



if __name__ == "__main__":
    app = MyApp()  # Object of class
    app.run()
