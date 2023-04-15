from socket import *
users = {}
serverPort = 18000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.send('succesfull server connection!\n'.encode())
    user_name = connectionSocket.recv(1024).decode()
    users[addr] = user_name, port
    print(users)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
connectionSocket.close()


