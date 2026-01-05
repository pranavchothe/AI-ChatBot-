import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env for local development
load_dotenv()

# Get API key safely
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found. Add it to .env or Streamlit Secrets.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Use a valid model
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("🤖 Simple Gemini Chatbot")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input.strip():
        response = model.generate_content(user_input)
        st.write("**Gemini Reply:**")
        st.write(response.text)
    else:
        st.warning("Please type a question")
