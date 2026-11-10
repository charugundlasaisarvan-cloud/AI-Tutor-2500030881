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

@klu.get("/student")
def student():
    return {"message":"Student details","name":"sai","id":1234,"course":"DSA","gender":"male","salary":50000}

@klu.get("/students")
def students():
    return [{"message":"Student details","name":"sai","id":1,"course":"DSA","gender":"male","salary":50000}, 
            {"message":"Student details","name":"sai1","id":2,"course":"ML","gender":"female","salary":60000}, 
            {"message":"Student details","name":"sai2","id":3,"course":"AI","gender":"male","salary":70000}
           ] 