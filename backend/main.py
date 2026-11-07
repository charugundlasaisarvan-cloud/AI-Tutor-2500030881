from fastapi import FastAPI
klu = FastAPI(title="AI-Tutor",
              description="AI Tutor pbl project",
              version="1.0.0")


@klu.get("/")
def home():
    return {"message": "Welcome to AI-Tutor porject!"}

@klu.get("/demo")
def demo():
    return {"message": "KL university!"}

@klu.get("/ask question")
def ask():
    return{"message":" what is LLM","Answer":"Large Language Model"}