import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 Simple Groq Chatbot")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        # Send request to Groq
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        st.write("**Groq Reply:**")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please type a question")
