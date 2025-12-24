import os
from langchain_google_genai import ChatGoogleGenerativeAI

print("API KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    temperature=0.2
)

response = llm.invoke("Say hello in one short sentence")
print(response.content)