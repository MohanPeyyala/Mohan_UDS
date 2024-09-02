import socket
import os

socket_file = '/tmp/get_sum'


client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


client_socket.connect(socket_file)
while(True):
    a=int(input("Enter a Number: "))
    
    client_socket.sendall(a.to_bytes(4, byteorder='big'))
    if(a==0):break
response = client_socket.recv(1024)
num_rec = int.from_bytes(response, byteorder='big')

print(num_rec)



client_socket.close()
