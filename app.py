from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import os
import gradio as gr


os.environ["OPENAI_API_KEY"] = ""  # Replace with your key

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content
    return None

description = '<img src="buehler-logo.png" alt="Logo" style="width:100px;"/><br/>A GPT-based nutrition assistant'

gr.ChatInterface(fn = predict, title = "Smart AI Nutritionist", description = description,).launch()