import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to ChatAI 👋")

st.sidebar.success("Select a feature above.")

st.markdown(
    """
    Greetings, future AI enthusiast!

    ChatAI is a chatbot that can answer your questions about almost anything.

    It has amazing capabilities and is currently in development.

    Some of it's capabilities include: Question Answering, Image Generation, Image Summerization, PDF summerization.

    
    Developed with ❤️ by Prathamesh Zade, Nikhil Sonone, Abhishek Gambhire and Chaitanya Sonawane.
    """
)
