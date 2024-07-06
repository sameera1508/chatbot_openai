from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API key",key="chatbot_api_key",type="password")
st.title("🎶🍨 Chatbot")
st.caption("🎢 A streamlit chatbot created by SS")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant","content": "How can i help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("please add your openai api key.")
        st.stop()
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    response=client.chat.completions.create(model="gpt-3.5-turbo",messages=st.session_state.messages)
    msg=response.choices[0].message.content
    st.session_state.messages.append({"role":"assistant","content":msg})
    st.chat_message("assistant").write(msg)
