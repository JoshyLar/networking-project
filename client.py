from socket import *
from threading import Thread
from datetime import datetime

serverName = 'localhost'
serverPort = 18001

# TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Connection Successful.")
print("Please Select an Option:")
print("Option 1: Get Chatroom Report")
print("Option 2: Join Chatroom")
print("Option 3: Quit Program")

verify = clientSocket.recv(1024)
address = clientSocket.recv(1024)
print(verify.decode())
print(address)


def listen_chat():
    while True:
        chat = clientSocket.recv(1024).decode()

        print("\n" + chat)


def join_failed(flag):
    string = flag.split(",")
    if string[0] == "JOIN_REQUEST_FLAG = 1":
        print("chat room joined. Username: ", string[1])

    elif string[0] == "JOIN_REQUEST_FLAG = 0":
        print("join failed, user name", string[1], " not available")


temp_thread = Thread(target=listen_chat)
temp_thread.daemon = True
temp_thread.start()

# user options
while True:
    sentence = input()

    if sentence.lower() == "option 1":
        clientSocket.send('ABCDEFG'.encode())

    if sentence.lower() == "option 2":
        sentence = "JOIN_REJECT_FLAG"
        username = input("Enter your username: ")
        clientSocket.send(sentence.encode())
        clientSocket.send(username.encode())
        # decode message for potential flags
        join_failed(clientSocket.recv(1024).decode())

    if sentence.lower() == "option 3":
        clientSocket.send('ZYXWVUT'.encode())
        break

    # message sent with username and timestamp
    sentence = username + ": " + sentence
    curr_time = datetime.now().strftime("[%H:%M:%S] ")
    sentence = curr_time + sentence

    clientSocket.send(sentence.encode())

# close clientSocket
clientSocket.close()
print("Socket Closed")
