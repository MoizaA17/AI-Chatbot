import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the client (automatically picks up GEMINI_API_KEY from environment)
client = genai.Client(  # Updated to use the imported Client
    api_key=API_KEY
)

st.set_page_config(page_title="AI Chatbot with Memory", page_icon="🤖")  #tab (Streamlit ❌ AI Chatbot with Memory 🤖 ✔)
st.title("AI Chatbot with Memory")

#Initialize UI Session State memory list if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state["messages"] = []

chat = client.chats.create(
    model="gemini-3.6-flash",
    history=[
        types.Content(
            role=msg["role"],
            parts=[types.Part.from_text(text=msg["content"])]
        )
        for msg in st.session_state.messages
    ]
)

#  Render past conversation in UI
for message in st.session_state.messages:
    # Convert 'model' role to Streamlit's 'assistant' label for display
    display_role = "assistant" if message["role"] == "model" else "user"
    with st.chat_message(display_role):
        st.markdown(message["content"])

#  Capture user input from chat box
if prompt := st.chat_input("Type your message here..."):
    # Display user input immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Save user prompt to Session State
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        # Send message to Gemini chat session
        response = chat.send_message(prompt)
        
        # Display Gemini response
        with st.chat_message("assistant"):
            st.markdown(response.text)
    
        # Save Gemini response to Session State
        st.session_state.messages.append({"role": "model", "content": response.text})

    except Exception as e:
        st.error(f"Error: {e}")