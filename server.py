import socket
from threading import Thread




def listen(client):
    while True:
        msg = connectionSocket.recv(1024).decode()
        try:
            if msg == "REPORT_REQUEST_FLAG=1":
                string = "REPORT_REQUEST_FLAG=1\n" + "number of users: " + str(len(users)) + "\n"
                for i in users:
                    string = string + "ip = " + str(i[1]) + " port= " + str(i[2]) + "\nuser name= " + i[3] + "\n"
                connectionSocket.send(string.encode())

            if msg == "JOIN_REJECT_FLAG":
                print("join requested")
                user_name = connectionSocket.recv(1024).decode()
                for i in users:
                    if i[3] == user_name:
                        string = "JOIN_REJECT_FLAG = 0, " + user_name
                        connectionSocket.send(string.encode())
            users.append((connectionSocket, IP, Port, user_name))
            string = "JOIN_REQUEST_FLAG = 1," + user_name
            connectionSocket.send(string.encode())
            history = "History: "
            for i in messages:
                history = history + i
            connectionSocket.send(history.encode())
            for i in users:
                string = user_name + " has joined the chat"
                i[0].send(string.encode())


            if msg == "q":
                print("Client Disconnected")
                for i in users:
                    if i[0] == connectionSocket:
                        users.remove(i)
                        connectionSocket.close()
                for i in users:
                    string = user_name + " has left the chat"
                    i[0].send(string.encode())
                
        except:
            a = 0




if __name__ == '__main__':
    users = []
    messages = []

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
        connectionSocket.send('server connection acknowledged\n'.encode())




        thread = Thread(target=listen, args = (connectionSocket,))

        thread.daemon = True

        thread.start()



    for connectionSocket in users:
        connectionSocket.close()

    serverSocket.close()
