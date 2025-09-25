from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
request = "GET /index.html HTTP/1.1 \r\nHost: localhost\r\n\r\n"
clientSocket.send(request.encode())
response = clientSocket.recv(1024)
print ('From Server:', response.decode())
clientSocket.close()