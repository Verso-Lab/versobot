import streamlit as st


def set_up_page(page_title, layout="centered", initial_sidebar_state="auto"):
    page_config = {
        "page_title": f"{page_title} • Versobot",
        "page_icon": "assets/verso_icon_with_bg.png",
        "layout": layout,
        "initial_sidebar_state": initial_sidebar_state,
    }
    st.set_page_config(**page_config)
    st.logo("assets/verso_logo.png", icon_image="assets/verso_icon.png")


def get_openai_api_key():
    """Retrieve the OpenAI API key from Streamlit secrets."""
    return st.secrets["OPENAI_API_KEY"]
