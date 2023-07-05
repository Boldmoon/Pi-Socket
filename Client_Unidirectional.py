import socket
HEADER = 64
PORT = 5555
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Ofline"
SERVER = "65.0.209.75"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)



while True:
    a = input("Please text to chat: ")
    send(a)
    if a == "exit":
        send(DISCONNECT_MESSAGE)
        exit()