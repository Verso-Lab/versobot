import streamlit as st


def initialize_session_states():
    """Initialize session states"""
    if 'chat' not in st.session_state:
        st.session_state.chat = False
    if 'source_text' not in st.session_state:
        st.session_state.source_text = None
    if 'initial_state' not in st.session_state:
        st.session_state.initial_state = []


def chat_button(button_placeholder, text, key=None, primary=False):
    """Spawn chat button in button_placeholder"""
    return button_placeholder.button(text,
                                     type="primary" if primary else "secondary",
                                     key=key)


def reset_chat():
    """Reset chat session state"""
    st.session_state.chat = False
    st.session_state.initial_state = st.session_state.chat_history = []
    if 'thread_id' in st.session_state:
        del st.session_state.thread_id
    st.session_state.latest_user_prompt = ""