from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from langchain_llm_streamer import stream_print


model = ChatOpenAI(
    api_key="***",  # Replace with your OpenAI API key
    model="gpt-3.5-turbo",
)

messages = [
    SystemMessage(content="You are a friendly AI. Please respond to the user's prompt."),
    HumanMessage(content="Tell me something about yourself.")
]

# Example usage
stream_print(model, messages)
