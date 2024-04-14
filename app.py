import chainlit as cl
from dotenv import load_dotenv
load_dotenv()
from langchain_community.chat_models.databricks import ChatDatabricks
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()

chat = ChatDatabricks(endpoint='databricks-dbrx-instruct')

@cl.on_message
async def main(message: cl.Message):
    response = chat.invoke(message.content)

    # Send a response back to the user
    await cl.Message(
        content=f"Response: {response.content}",
    ).send()

