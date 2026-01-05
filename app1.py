import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("🤖 Simple Gemini Chatbot")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=user_input
        )
        st.write("**Gemini Reply:**")
        st.write(response.text)
    else:
        st.warning("Please type a question")
