import os
import socket
result=0
socket_file='/tmp/get_sum'
if os.path.exists(socket_file):
    os.remove(socket_file)

server_socket=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_socket.bind(socket_file)

server_socket.listen(1)

print("Server is Listening")

client_socket,client_addr=server_socket.accept()

print("Client Connected")
while(True):
    data=client_socket.recv(1024)
    Num_res=int.from_bytes(data, byteorder='big')
    if(Num_res!=0):
        result=result+Num_res
    else: 
        client_socket.sendall(result.to_bytes(4, byteorder='big'))
        break
client_socket.close()
server_socket.close()
os.remove(socket_file)
