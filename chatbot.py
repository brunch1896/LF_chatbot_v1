import openai
import streamlit as st
import os

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# openai_api_key = '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'

st.title("💬 颖鸿之家问答机器人")
# openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你想问什么问题？"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    # openai.api_key = openai_api_key
    openai.api_key = os.getenv('OPENAI_API_KEY') 
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
