import socket 

IP = '127.0.0.1'
port = 7000
serverSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
serverSocket.bind((IP , port))

serverSocket.listen(2)
while True : 
    client, Address = serverSocket.accept()
    message = client.recv(1024)
    if('file_content' in message.decode()):
        file_server = open('server_file.txt' , 'r')
        currnt_chunck = file_server.readline()
        while True: 
            if ( currnt_chunck != ""):
                client.send(currnt_chunck.encode())
                currnt_chunck = file_server.readline()
            else : 
                client.send("end".encode()) 
                client.close()
                break
