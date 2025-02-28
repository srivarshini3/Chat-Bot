import os
import streamlit as st
import google.generativeai as genai

# Configure API Key securely
API_KEY = "AIzaSyAxxjNAXVkdTtjsc6wuhyYVdZc5WZvj4fE"
genai.configure(api_key=API_KEY)

# Initialize the Generative Model
m = genai.GenerativeModel('gemini-1.5-flash')

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = m.start_chat(history=[])

st.title("Chat-Bot")
st.write("This is a chatbot to answer queries.")

# Store chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input and process response
if prompt := st.chat_input("Say something"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Gemini API
    response = st.session_state.chat.send_message(prompt)

    # Append response to session state and display it
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)
