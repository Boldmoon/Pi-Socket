import socket


def client_program():
    host = "65.0.209.75"
    port = 5555
    client_socket = socket.socket()
    client_socket.connect((host, port))
    main = "pi"
    client_socket.send(main.encode())
    while True:
        client_socket.recv(1024).decode()

