import socket 

IP = '127.0.0.1'
port = 7001
serverSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
serverSocket.bind((IP , port))

serverSocket.listen(1)
while True : 
    client, Address = serverSocket.accept()
    message = client.recv(1024)
    if('local_server' in message.decode()  ):
        client.send(f"{IP}-{7000}" .encode())
        
