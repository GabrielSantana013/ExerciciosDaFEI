from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pessoa(BaseModel):
    nome: str
    sobrenome: str
    idade: int

class Tarefa(BaseModel):
    tarefa: str
    prioridade: int
    feito: bool

@app.post("/pessoa/")
def criar_pessoa(pessoa: Pessoa):
    return pessoa

@app.get("/")
def root():
    return {"message": "hello world"}

counter = 0
@app.get("/count")
def get_count():
    global counter    
    counter += 1
    return counter

@app.get("/hello")
def get_name(name):
    return f"Olá, invocador"

@app.get("/hello/{name}")
def get_name(name):
    return f"Hello, {name}"

@app.get("/hello/")
def hello(parammeter="World"):
    return f"Hello, {parammeter}"

tarefas = list()

@app.get("/")
def root():
    return tarefas

@app.get("/tarefa/{pos}")
def get_tarefa(pos: int):
    return tarefas[pos]

@app.post("/adicionar/")
def criar_tarefa(tarefa: Tarefa):
    tarefa.feito = False
    tarefas.append(tarefa)
    return len(tarefas)

@app.put("/feito/{pos}")
def marcar_feito(pos: int):
    tarefas[pos].feito = True
    return tarefas[pos]

@app.delete("/deletar/{pos}")
def deletar_tarefa(pos: int):
    tarefa = tarefas.pop(pos)
    return tarefa
