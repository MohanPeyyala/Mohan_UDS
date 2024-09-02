import socket
import os

socket_file = '/tmp/my_unix_socket'


client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


client_socket.connect(socket_file)
try:
    while(True):
        a=input("Enter a Message: ")
        if(a=='0'):break
        client_socket.sendall(a.encode('utf-8'))

        response = client_socket.recv(1024)
        print("Received:", response.decode())
except Exception as e:
    print("Server is closed: ",e)
client_socket.close()

