from langchain_openai import ChatOpenAI #import chat wrapper
from langchain.memory import ConversationBufferMemory  #stores full convo automatically
from langchain.chains import ConversationChain

HF_API_KEY = "Your API Key"


llm=ChatOpenAI(
    openai_api_key=HF_API_KEY,
    base_url="https://router.huggingface.co/v1",   #writing code to merge with LLM by langchain 
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    temperature=0.7,
    max_tokens=200
)

memory = ConversationBufferMemory()
#stores the entire history


conversation = ConversationChain(
    llm=llm,
    memory=memory
)#combining process

print("🤖 Chatbot started! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye 👋")
        break

    response = conversation.predict(input=user_input)

    print("Bot:", response)