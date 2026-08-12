from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/petters")
    return {"message": "Pedrão pica dura"}
