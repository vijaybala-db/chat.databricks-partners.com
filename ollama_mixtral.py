from langchain.chat_models.ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema.output_parser import StrOutputParser
llm = ChatOllama(model='mixtral', stream=True)
memory = ConversationBufferMemory()
#chain = ConversationChain(llm=llm, memory=memory)
chain = llm | StrOutputParser()
generator = chain.stream('What tree fits in your hand?')
for token in generator:
    print(token, flush=True, end='')