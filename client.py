from socket import *
from threading import Thread
from datetime import datetime

serverName = 'localhost'
serverPort = 18003

# TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))



print("Connection Successful.")
print(clientSocket.recv(1024).decode())
print("Please Select an Option:")
print("Option 1: Get Chatroom Report")
print("Option 2: Join Chatroom")
print("Option 3: Quit Program")

#verify = clientSocket.recv(1024)
#address = clientSocket.recv(1024)
#print(verify.decode())
#print(address)

def send_msg():

    # message sent with username and timestamp
    sentence = username + ": " + sentence
    curr_time = datetime.now().strftime("[%H:%M:%S] ")
    sentence = curr_time + sentence

    clientSocket.send(sentence.encode())

def listen_chat():
    while True:
        chat = clientSocket.recv(1024).decode()
        string = chat.split(",")
        print(string[0], " verify")
        if string[0] == 'JOIN_REQUEST_FLAG = 1':
            print("chat room joined. Username: ", string[1])

        elif string[0] == 'JOIN_REQUEST_FLAG = 0':
            print("join failed, user name", string[1], " not available")
            
        
        print("\n" + chat)


def join_failed(flag):
    string = flag.split(",")
    print(string[0], " verify")
    if string[0] == 'JOIN_REQUEST_FLAG = 1':
        print("chat room joined. Username: ", string[1])

    elif string[0] == 'JOIN_REQUEST_FLAG = 0':
        print("join failed, user name", string[1], " not available")

temp_thread = Thread(target=listen_chat)
temp_thread.daemon = True
temp_thread.start()


# user options
while True:
    sentence = input()
    print(sentence)
    if sentence.lower() == 'option 1'or sentence.lower() == '#a':
        clientSocket.send('REPORT_REQUEST_FLAG=1'.encode())

    if sentence.lower() == 'option 2' or sentence.lower() == '#b':
        sentence = "JOIN_REJECT_FLAG"
        clientSocket.send(sentence.encode())
        username = input("Enter your username: ")
        clientSocket.send(username.encode())
        # decode message for potential flags


    if sentence.lower() == 'option 3'or sentence.lower() == '#c':
        clientSocket.send('ZYXWVUT'.encode())
        break



# close clientSocket
clientSocket.close()
print("Socket Closed")
