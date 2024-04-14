from langchain.chat_models.ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
llm = ChatOllama(model='mixtral')
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory)
response = chain.invoke('What tree fits in your hand?')
print(response)