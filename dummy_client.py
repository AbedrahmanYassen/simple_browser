import socket 
import re


clientSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1' , 7001))
url = 'http//local_server/file_content' 

def getUrlAddrees(string):
    clientSocket.send(string.encode())
    message = clientSocket.recv(1024)
    IP = re.findall("(.*)-", message.decode())
    port = re.findall("-(.*)", message.decode())
    return (IP[0] , int(port[0]))
