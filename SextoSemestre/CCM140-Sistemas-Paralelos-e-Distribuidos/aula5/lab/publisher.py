import os
import zmq
from time import time, sleep
import random

process = os.getenv("PROCESS")

context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.connect("tcp://proxy:5555")

sleep(5)

while True:

    if process == "P1":
        message = f"HORARIO P1:{time()}"
    else:
        message = f"RANDOM P2:{random.randint(1, 6)}"

    socket.send_string(message)

    print(f"{process}: {message}", flush=True)
    sleep(1)
