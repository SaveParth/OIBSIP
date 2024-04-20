import socket
from threading import Thread

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print("Received from client:", data)
        except Exception as e:
            print("Error receiving message from client:", e)
            break

def send_messages(client_socket):
    while True:
        try:
            message = input("Enter message to send to client: ")
            client_socket.send(message.encode())
        except Exception as e:
            print("Error sending message to client:", e)
            break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))

server_socket.listen(5)
print("Server listening...")

client_socket, addr = server_socket.accept()
print('Got connection from', addr)


receive_thread = Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = Thread(target=send_messages, args=(client_socket,))
send_thread.start()
