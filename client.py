from socket import *
from threading import Thread
from datetime import datetime



#verify = clientSocket.recv(1024)
#address = clientSocket.recv(1024)
#print(verify.decode())
#print(address)

def send_chat(clientSocket):
    while True:
        sentencew = ""
    # message sent with username and timestamp
        #sentence  =  input(f"{user_name}: " )
        curr_time = datetime.now().strftime("[%H:%M:%S] ")
        sentence = input()

        if sentence.lower() != "#quit":
                sentence = user_name + ": " + sentence
                curr_time = datetime.now().strftime("[%H:%M:%S] ")
                sentence = curr_time + sentence
                clientSocket.send(sentence.encode())

        elif sentence.lower() == "#quit":
                clientSocket.send("QUIT_REQUEST_FLAG".encode())
                break



def listen_chat(client):
    while True:
        chat = client.recv(1024).decode()
        if chat != "QUIT_ACCEPT_FLAG":
            print(chat)
        else:
            break


if __name__ == '__main__':
    serverName = "localhost"
    serverPort = 18000

    # TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    user_name = ""

    print("Connection Successful.")
    print(clientSocket.recv(1024).decode())
    print("Please Select an Option:")
    print("Option 1: Get Chatroom Report")
    print("Option 2: Join Chatroom")
    print("Option 3: Quit Program")

    while True:
        msg = input("option:")
        if msg == "2":
            print("Option 2 selected")
            clientSocket.send("JOIN_REQUEST_FLAG".encode())
            msg = clientSocket.recv(1024).decode()
            if msg == "JOIN_REQUEST_FLAG = 1":
                flag = 0
                while flag == 0:
                    user_name = input("Choose username: ")
                    clientSocket.send(user_name.encode())
                    if clientSocket.recv(1024).decode() == "JOIN_ACCEPT_FLAG = 1":
                        print(f"user name selected = {user_name}")
                        while True:
                            listen_thread = Thread(target=listen_chat, args=(clientSocket,))
                            send_thread = Thread(target=send_chat, args=(clientSocket,))
                            listen_thread.daemon = True
                            send_thread.daemon = True
                            listen_thread.start()
                            send_thread.start()
                        break
                    else:
                        print("username in use")

                break
            else:
                print("Chat room full")
                clientSocket.close()
                exit()

        elif msg == "1":
            print("Option 1 selected")
            clientSocket.send("REPORT_REQUEST_FLAG".encode())
            print(clientSocket.recv(1024).decode())

        elif msg == "3":
            print("option 3 selected")
            clientSocket.send("QUIT_REQUEST_FLAG".encode())
            print("Goodbye")
            break
        else:
            break











# user options
#while True:
 #   sentence = input()
  #  sentence = username + ": " + sentence
  #  curr_time = datetime.now().strftime("[%H:%M:%S] ")
   # sentence = curr_time + sentence
   # clientSocket.send(sentence.encode())





# close clientSocket
    clientSocket.close()
    print("Socket Closed")
