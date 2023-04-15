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

username = input("Enter your username: ")


def listen_chat():
    while True:
        chat = clientSocket.recv(1024).decode()
        print("\n" + chat)


temp_thread = Thread(target=listen_chat)
temp_thread.daemon = True
temp_thread.start()

while True:
    sentence = input()

    if sentence.lower() == "option 1":
        clientSocket.send('ABCDEFG'.encode())

    if sentence.lower() == "option 2":
        clientSocket.send(sentence.encode())

    if sentence.lower() == "option 3":
        clientSocket.send('ZYXWVUT'.encode())
        break

    sentence = username + ": " + sentence
    curr_time = datetime.now().strftime("[%H:%M:%S] ")
    sentence = curr_time + sentence

    clientSocket.send(sentence.encode())

# close clientSocket
clientSocket.close()
print("Socket Closed")
