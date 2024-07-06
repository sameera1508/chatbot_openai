# chatbot_openai

This project is a simple chatbot application built using Streamlit and OpenAI's GPT-3.5-turbo model. It allows users to interact with the chatbot through a web interface.

## Features

- User-friendly chat interface
- Secure input for OpenAI API key
- Real-time interaction with OpenAI's GPT-3.5-turbo model

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI Python client library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your OpenAI API key in the sidebar.

4. Start chatting with the chatbot!

## Code Explanation

### `app.py`

The main application code:

```python
from openai import OpenAI
import streamlit as st

# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API key", key="chatbot_api_key", type="password")

# Main interface
st.title("🤖 Chatbot")
st.caption("A streamlit chatbot created by SS")

# Initialize chat messages in session state if not already done
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    # Check if OpenAI API key is provided
    if not openai_api_key:
        st.info("please add your openai api key.")
        st.stop()

    # Create an OpenAI client with the provided API key
    client = OpenAI(api_key=openai_api_key)
    
    # Append user's message to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Generate a response from the OpenAI API
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    
    # Append assistant's response to session state and display it
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
