import chainlit as cl
from dotenv import load_dotenv
load_dotenv()
from langchain_community.chat_models.ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.schema.output_parser import StrOutputParser
memory = ConversationBufferMemory()

llm = ChatOllama(model='mixtral', stream=True)
chain = llm | StrOutputParser()

@cl.on_chat_start
async def start():
    await cl.Message(content='Welcome to the Databricks booth at Slalom Innovation Day!').send()

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content='')
    stream = chain.astream(message.content)
    async for part in stream:
        await msg.stream_token(part)

