import socket

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Server listening on port 9999...")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")
    data = client.recv(1024).decode()
    print("ALERT:", data)
    client.close()