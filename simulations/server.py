import os
import socket
socket_file='/tmp/my_unix_socket'
if os.path.exists(socket_file):
    os.remove(socket_file)

server_socket=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_socket.bind(socket_file)

server_socket.listen(1)

print("Server is listening")

client_socket,client_address=server_socket.accept()

print("Client Connected")
try:
    while(True):
        data=client_socket.recv(1024)

        print("Received: ",data.decode())
        a=input("Enter a Msg")
        if(a=='0'):exit(0)
        client_socket.sendall(a.encode('utf-8'))
except Exception as e:
    print("Client is Not Active",e)
server_socket.close()
client_socket.close()
os.remove(socket_file)

