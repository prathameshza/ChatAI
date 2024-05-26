import getpass
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Provide your Google API Key")

llm = ChatGoogleGenerativeAI(model="gemini-pro")

st.set_page_config(
    page_title="Question Answering",
    page_icon="❔",
)

st.title("Chatbot")

user_input = st.text_input("Type your question here:")

if user_input:
    result = llm.invoke(user_input)
    st.write(result.content)