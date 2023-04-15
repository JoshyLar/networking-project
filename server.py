import socket
from threading import Thread




def listen(client):
 string = "added"
 for i in users:
    string = string + "ip = " + str(i[1]) + ", port= " + str(i[2]) + ", user name= " + i[3] + "number of users " + str(len(users)) + "\n"
 print(string)

 while True:
    msg = client.recv(1024).decode()

    try:
        if msg == "REPORT_REQUEST_FLAG=1":
            string = "REPORT_REQUEST_FLAG=1\n" + "number of users" + str(len(users))+ "\n"
            for i in users:
                string = string + "ip = " + str(i[1]) + " port= " + str(i[2]) + "user name= " + i[3] + "\n"
            print(string)
            connectionSocket.send(string.encode())

        if msg == "JOIN_REQUEST_FLAG":
            user_name = client.recv(1024).decode()
            for i in users:
                if user_name == i[3]:
                    string = "JOIN_REQUEST_FLAG = 0, " + user_name
                    client.send(string.encode())
                else:
                    for i in users:
                        if i[0] == client:
                            i[3] = user_name
                    string = "JOIN_REQUEST_FLAG = 1, " + user_name
                    client.send(string.encode())


        if msg == "q":
            print("Client Disconnected")
            for i in users:
                if i[0] == client:
                    users.remove(i)
                    client.close()
            client.close()

    except:

        print("Error")
        for i in users:
            if i[0] == client:
                users.remove(i)
                client.close()

    for connectionSocket in users:
        connectionSocket.send(msg.encode())


if __name__ == '__main__':
    users = []

    server_port = 18003
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
        users.append((connectionSocket,IP,Port,""))



        thread = Thread(target=listen, args = (connectionSocket,))

        thread.daemon = True

        thread.start()

    for connectionSocket in users:
        connectionSocket.close()

    serverSocket.close()
