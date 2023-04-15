from socket import *
serverName = 'localhost'
serverPort = 18000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
verify = clientSocket.recv(1024)
address = clientSocket.recv(1024)
print(verify.decode())
print(address)
while(1):
        sentence = input('Enter username')
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print ('From Server:', modifiedSentence.decode())
clientSocket.close()
