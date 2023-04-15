import socket
from threading import Thread





def listen(client):
 string = "REPORT_REQUEST_FLAG=1\n" + "number of users: " + str(len(users)) + "\n"
 for i in users:
    string = string + "ip = " + str(i[1]) + ", port= " + str(i[2]) + ", user name= " + i[3] + "\n"
 print(string)
 while True:
    msg = client.recv(1024).decode()

    try:
        if msg == "REPORT_REQUEST_FLAG=1":
            string = "REPORT_REQUEST_FLAG=1\n" + "number of users" + str(len(users))+ "\n"
            for i in users:
                string = string + "ip = " + str(i[1]) + " port= " + str(i[2]) + "user name= " + i[3] + "\n"
            print(string)
            connectionSocket.send("hey".encode())

        if msg == "q":
            print("Client Disconnected")
            users.remove(connectionSocket)
            connectionSocket.close()

    except:

        print("Error")
        users.remove(connectionSocket)
    for connectionSocket in users:
        connectionSocket.send(msg.encode())


if __name__ == '__main__':
    users = []

    server_port = 18002
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
        IP,Port = addr
        connectionSocket.send('succesfull server connection!\n'.encode())
        user_name = connectionSocket.recv(1024).decode()
        users.append((connectionSocket,IP,Port,user_name))



        thread = Thread(target=listen, args = (connectionSocket,))

        thread.daemon = True

        thread.start()

    for connectionSocket in users:
        connectionSocket.close()

    serverSocket.close()
