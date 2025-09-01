from dotenv import load_dotenv
import os
load_dotenv()

#from langchain_ollama import OllamaLLM

#llm = OllamaLLM(model="llama3.1:8b") 

def main():
    print("Hello from gen-ai!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
