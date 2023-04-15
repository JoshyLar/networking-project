import socket
from threading import Thread





def listen(client):
 while True:
    msg = client.recv(1024).decode()
    for connectionSocket in users:
        connectionSocket.send(msg.encode())


if __name__ == '__main__':
    users = set()

    server_port = 18001
    host_name = 'local host'

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = socket.gethostname()
    server_ip = socket.gethostbyname(name)  # get the server ip
    serverSocket.bind(('', server_port))

    print("server IP= ", server_ip, "port= ", server_port)
    print('The server is ready to receive')
    serverSocket.listen(3)

    while True:
        connectionSocket, addr = serverSocket.accept()
        connectionSocket.send('succesfull server connection!\n'.encode())
        users.add(connectionSocket)


        thread = Thread(target=listen, args = connectionSocket)

        thread.daemon = True

        thread.start()

    for connectionSocket in users:
        connectionSocket.close()

    serverSocket.close()
