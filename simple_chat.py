import streamlit as st
from components.chat import versobot
from utils.session import initialize_session_states, chat_button, reset_chat
from utils.config import set_up_page


# App setup
set_up_page("Chat", layout="wide")
initialize_session_states()

versobot(assistant_id="asst_i5ylsjPx1CWwe0xJFOOQ80yC",
         initial_message="Hi, I'm **Versobot!** How can I help?")