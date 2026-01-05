import streamlit as st
import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Correct model
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("AI Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
