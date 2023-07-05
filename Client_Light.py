import socket
import time


def client_program():
    host = "65.0.209.75"
    port = 5555
    client_socket = socket.socket()
    client_socket.connect((host, port))
    main = "cli"
    client_socket.send(main.encode())
    while True:
        message = input("On or Off ")
        if (message == "on") or (message == "ON") or (message == "On") or (message == "oN") or (message == "O") or (
                message == "o"):
            messaged = "on"
            client_socket.send(messaged.encode())
            continue
        elif (message == "off") or (message == "OFF") or (message == "Off") or (message == "F") or (message == "f"):
            messaged = "off"
            client_socket.send(messaged.encode())
            continue
        elif (message == "S") or (message == "s"):
            messaged = "bye"
            client_socket.send(messaged.encode())
            time.sleep(5)
            client_socket.close()
            break
        else:
            print("\n Enter a valid input")
            continue
    client_socket.close()


client_program()
