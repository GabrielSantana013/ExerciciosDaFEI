import zmq
from time import sleep
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

# i = 0
# while True:
#     print(f"Mensagem {i}:", end=" ", flush=True)
#     socket.send(b"Hello")
#     mensagem = socket.recv()
#     print(f"{mensagem}")
#     i += 1
#     sleep(0.5)

#Adicionar tarefas
def criar_tarefa(i):
    tarefa1 = {
        "name": "Super tarefa",
        "id": {i}        
    }
    

#Remover tarefas

def remover_tarefa(tarefas, id):
    


#Listar tarefas
