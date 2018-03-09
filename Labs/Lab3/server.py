import zmq
import time
import threading

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock1 = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5680")
sock1.bind("tcp://127.0.0.1:5677")

mess = ""
prev_mess = ""

def in_thread():
    global mess, prev_mess
    mess = sock1.recv_string()
    sock1.send_string("")
    prev_mess = mess
    while True:
        mess = sock1.recv_string()
        sock1.send_string("")
    
def out_thread():
    global mess, prev_mess
    while True:
        if prev_mess != mess:
            messages = mess.split(" ",1)
            sock.send_string(messages[0]+" : "+messages[1])
            prev_mess = mess

thread1 = threading.Thread(target=in_thread)
thread2 = threading.Thread(target=out_thread)

thread1.start()
thread2.start()



