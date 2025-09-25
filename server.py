from socket import *
import webbrowser

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()
    print("Request: " + request)

    request_line = request.splitlines()[0]
    method, path, version = request_line.split()

    if path == "/":
        path = "/index.html"

    filename = path.lstrip("/")

    try:
        with open(filename, "r") as f:
            body = f.read()
        response = (
            "HTTP/1.1 200 OK \r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
            + body            
        )
        webbrowser.open(filename)
    except FileNotFoundError:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "\r\n"
            f"<h1>404 Not Found: {path}</h1>"
        )
    connectionSocket.send(response.encode())
    connectionSocket.close()

