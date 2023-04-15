from socket import *
from threading import Thread
import time
from datetime import datetime

serverName = 'localhost'
serverPort = 18000

# TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Connection Successful.")
print("Type q to exit chatroom")

verify = clientSocket.recv(1024)
address = clientSocket.recv(1024)
print(verify.decode())
print(address)

username = input("Enter your a username: ")


def listen_chat():
    while True:
        chat = clientSocket.recv(1024).decode()
        print("\n" + chat)


temp_thread = Thread(target=listen_chat)
temp_thread.daemon = True
temp_thread.start()

while True:
    sentence = input()

    if sentence.lower() == "q":
        clientSocket.send(sentence.encode())
        break

    sentence = username + ": " + sentence
    curr_date = datetime.now().strftime("[%H:%M] ")
    sentence = curr_date + sentence

    clientSocket.send(sentence.encode())

# close clientSocket
clientSocket.close()
