import streamlit as st


def set_up_page(page_title, layout="centered", initial_sidebar_state="auto"):
    """
    Set up the Streamlit page configuration and display the Verso logo.

    Args:
        page_title (str): The page title, which displays between "Versobot" and "· Streamlit".
        layout (str, optional): The layout of the page. Defaults to "centered".
        initial_sidebar_state (str, optional): The initial state of the sidebar. Defaults to "auto".

    Returns:
        None
    """
    page_config = {
        "page_title": f"Versobot {page_title}",
        "page_icon": "assets/verso_icon_with_bg.png",
        "layout": layout,
        "initial_sidebar_state": initial_sidebar_state,
    }
    st.set_page_config(**page_config)
    st.logo("assets/verso_logo.png", icon_image="assets/verso_icon.png")


def get_openai_api_key():
    """Retrieve the OpenAI API key from Streamlit secrets."""
    return st.secrets["OPENAI_API_KEY"]
