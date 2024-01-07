import socket


server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print("Waiting for connection...")

connection, client_address = server_socket.accept()
print("Connected to", client_address)

try:
    while True:
        data = connection.recv(1024)
        if data:
            print("Received data:", data.decode('utf-8'))
        else:
            break
finally:
    connection.close()
    server_socket.close()
