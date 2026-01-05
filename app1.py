import streamlit as st
import os
import google.generativeai as genai

st.title("🤖 Simple Gemini Chatbot")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        response = model.generate_content(user_input)
        st.write("**Gemini Reply:**")
        st.write(response.text)
    else:
        st.warning("Please type a question")
