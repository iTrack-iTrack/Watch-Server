import socket

def initialise():
    server = socket.socket()
    port = 8081

    server.bind(("",port))
    server.listen(5)

    server.settimeout(1)

    return server

def receive(server):
    try:
        client, address = server.accept()

        message = client.recv(1024).decode().rstrip()

        return message
    except socket.timeout:
        return None

def terminate(server):
    server.close()
