from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gemini-2.5-flash",
    temperature=0.2
)
