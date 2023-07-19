import streamlit as st
from models.chat_model import ChatModel
from views.chat_view import ChatView

def main():
    st.set_page_config(
        page_title="ChatGPTMimic",
        page_icon="🧠"
    )
    st.header("ChatGPTMimic")

    model = ChatModel()
    view = ChatView(model)
    view.display_chat()

if __name__ == '__main__':
    main()
