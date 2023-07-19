from langchain.chat_models import ChatOpenAI

class ChatModel:
    def __init__(self, temperature=0):
        self.llm = ChatOpenAI(temperature=temperature)

    def get_response(self, messages):
        return self.llm(messages)
