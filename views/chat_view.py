import streamlit as st
from schemas.message import SystemMessage, HumanMessage, AIMessage

class ChatView:
    def __init__(self, model):
        self.model = model

    def display_chat(self):
        # チャット履歴の初期化
        if "messages" not in st.session_state:
            st.session_state.messages = [
                SystemMessage(content="You are a helpful assistant.")
            ]

        # ユーザーの入力を監視
        if user_input := st.chat_input("聞きたいことを入力してね！"):
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("ChatGPT is typing ..."):
                response = self.model.get_response(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))

        # チャット履歴の表示
        messages = st.session_state.get('messages', [])
        for message in messages:
            if isinstance(message, AIMessage):
                with st.chat_message('assistant'):
                    st.markdown(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message('user'):
                    st.markdown(message.content)
            else:  # isinstance(message, SystemMessage):
                st.write(f"System message: {message.content}")
