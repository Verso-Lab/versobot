import streamlit as st
import re
from openai import OpenAI
from openai.types.beta.assistant_stream_event import ThreadMessageDelta
from openai.types.beta.threads.text_delta_block import TextDeltaBlock
from utils.config import get_openai_api_key

OPENAI_API_KEY = get_openai_api_key()

def initialize_client():
    return OpenAI(api_key=OPENAI_API_KEY)


def create_thread(client):
    thread = client.beta.threads.create()
    return thread.id


def initialize_chat_history(initial_message):
    if "chat_history" not in st.session_state or not st.session_state.chat_history:
        st.session_state.chat_history = [
            {"role": "assistant", "content": initial_message}]


def display_chat_history():
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_query(placeholder, client, thread_id, assistant_id):
    if user_query := st.chat_input(placeholder):
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.chat_history.append(
            {"role": "user", "content": user_query})
        client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=user_query)
        stream_assistant_reply(client, thread_id, assistant_id)


def stream_assistant_reply(client, thread_id, assistant_id):
    with st.chat_message("assistant"):
        stream = client.beta.threads.runs.create(
            thread_id=thread_id, assistant_id=assistant_id, stream=True)
        assistant_reply_box = st.empty()
        assistant_reply = ""
        with st.spinner('Generating response...'):
            for event in stream:
                if isinstance(event, ThreadMessageDelta) and isinstance(event.data.delta.content[0], TextDeltaBlock):
                    assistant_reply_box.empty()
                    assistant_reply += event.data.delta.content[0].text.value
                    assistant_reply = re.sub("【.*?】", "", assistant_reply)
                    assistant_reply_box.markdown(assistant_reply)
                    break
        for event in stream:
            if isinstance(event, ThreadMessageDelta) and isinstance(event.data.delta.content[0], TextDeltaBlock):
                assistant_reply_box.empty()
                assistant_reply += event.data.delta.content[0].text.value
                assistant_reply = re.sub("【.*?】", "", assistant_reply)
                assistant_reply_box.markdown(assistant_reply)
        st.session_state.chat_history.append(
            {"role": "assistant", "content": assistant_reply})


def versobot(assistant_id, initial_message, placeholder="Chat with Versobot"):
    client = initialize_client()
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = create_thread(client)
    initialize_chat_history(initial_message)
    display_chat_history()
    handle_user_query(placeholder, client,
                      st.session_state.thread_id, assistant_id)
