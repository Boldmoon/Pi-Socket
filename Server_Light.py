import socket
from _thread import *

ServerSocket = socket.socket()
host = ''
port = 5555
ThreadCount = 0
ServerSocket.bind((host, port))
ServerSocket.listen(5)
pi = 0
count = 0
cli = 0


def threaded_client(connection):
    global count, pi, cli
    if connection.recv(1024).decode() == "pi":
        pi = connection
        count = 1
    elif connection.recv(1024).decode() == "cli":
        cli = connection
        count = 2


while True:
    if count == 2:
        break
    Client, address = ServerSocket.accept()
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1

while True:
    if cli.recv(1024).decode() == "on":
        sen = "on"
        pi.send(sen.encode())
    elif cli.recv(1024).decode() == "off":
        sen = "on"
        pi.send(sen.encode())
    elif cli.recv(1024).decode() == "s":
        cli.close()
        pi.close()
        break
ServerSocket.close()
