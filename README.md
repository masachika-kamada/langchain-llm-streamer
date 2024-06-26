# LangChain LLM Streamer

LangChain LLM Streamer is a Python package that allows you to stream and print responses from LangChain's language models in an asynchronous manner.

## Installation

You can install the package using pip:

```bash
pip install langchain-llm-streamer
```

## Usage

Here is an example of how to use the LangChain LLM Streamer:

```python
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
```
