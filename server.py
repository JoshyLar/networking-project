import socket
from threading import Thread


def listen(client):
    while True:
        msg = client.recv(1024).decode()
        if msg == "QUIT_REQUEST_FLAG":
            client.send("QUIT_ACCEPT_FLAG".encode())
            send(f"user {user_names[users.index(client)]} has left the chat".encode())
            client.close()
            print(f"user {user_names[users.index(client)]} quit")
            user_names.remove(users.index(client))
            users.remove(users.index(client))
            print(f"Number of  users: {len(users)}")
            break

    else:
        for user in users:
            if user != client:
                user.send(msg.encode())





def send(msg):
    for user in users:
        user.send(msg).encode()

def check_user_names(user_name):
    if len(user_names) != 0:
        for users in user_names:
            print(users)
            if user_name == users:
                return 0
    return 1


if __name__ == '__main__':
    users = []
    user_names = []
    user_addr = []
    messages = []
    chat_room_size = 3

    server_port = 18000
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
        print("join requested")
        connectionSocket.send('server connection acknowledged\n'.encode())
        while True:
            msg = connectionSocket.recv(1024).decode()
            print(msg)

            user_name_flag = 0

            if msg == "JOIN_REQUEST_FLAG":
                print("username requested")
                if (len(users) > chat_room_size + 1):
                    print("Chatroom full user rejected")
                    connectionSocket.send('JOIN_REJECT_FLAG'.encode())
                    connectionSocket.close()
                connectionSocket.send("JOIN_REQUEST_FLAG = 1".encode())


                while user_name_flag == 0:





                    user_name = connectionSocket.recv(1024).decode()
                    user_name_flag = check_user_names(user_name)
                    if user_name_flag == 0:
                        connectionSocket.send('JOIN_REJECT_FLAG'.encode())

                    else:
                        connectionSocket.send('JOIN_ACCEPT_FLAG = 1'.encode())
                        send(f"{user_name} has joined the chat".encode())
                        users.append(connectionSocket)
                        user_names.append(user_name)
                        user_addr.append(addr)
                        if len(messages) != 0:
                            history = ""
                            for i in messages:
                                history += history + i
                            connectionSocket.send(history.encode())
                        connectionSocket.send(f"Welcome to the chat {user_name}\n".encode())
                        thread = Thread(target=listen, args=(connectionSocket,))

                        thread.daemon = True

                        thread.start()
                        print(f"New user added. Number of  users: {len(users)}")
                        break


            elif msg == "REPORT_REQUEST_FLAG":
                print("report requested")
                if len(users) > 0:

                    string = ""
                    for i in range(len(user_names)):
                        string += user_names[i] + " ip: " + user_addr[i][0] + " port: " + user_addr[i][0] + "\n"
                        print(string)
                    connectionSocket.send(string.encode())
                else:
                    connectionSocket.send('chat room empty'.encode())
            elif msg == "QUIT_REQUEST_FLAG":
                connectionSocket.send("QUIT_ACCEPT_FLAG".encode())
                connectionSocket.close()
                print(f"user {connectionSocket} connection terminated")
                break











    msg = ""


    for connectionSocket in users:
        connectionSocket.close()

    serverSocket.close()

