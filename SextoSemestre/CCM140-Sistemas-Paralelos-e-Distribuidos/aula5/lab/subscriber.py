import zmq
import os

context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect("tcp://proxy:5556")

process = os.getenv("PROCESS")

print(f"PROCESS = {process}", flush=True)

if process == "SUB_P1":
    sub.setsockopt_string(zmq.SUBSCRIBE, "HORARIO")

elif process == "SUB_P2":
    sub.setsockopt_string(zmq.SUBSCRIBE, "RANDOM")

elif process == "SUB_P1_P2":
    sub.setsockopt_string(zmq.SUBSCRIBE, "HORARIO")
    sub.setsockopt_string(zmq.SUBSCRIBE, "RANDOM")

while True:
    message = sub.recv_string()
    print(f"{process} recebeu: {message}", flush=True)

sub.close()
context.close()
