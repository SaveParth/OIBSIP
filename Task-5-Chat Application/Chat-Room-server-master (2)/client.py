import socket
from threading import Thread

def receive_messages(server_socket):
    while True:
        try:
            data = server_socket.recv(1024).decode()
            if not data:
                break
            print("Received from server:", data)
        except Exception as e:
            print("Error receiving message from server:", e)
            break

def send_messages(server_socket):
    while True:
        try:
            message = input("Enter message to send to server: ")
            server_socket.send(message.encode())
        except Exception as e:
            print("Error sending message to server:", e)
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 12345

client_socket.connect((host, port))
print("Connected to server")

receive_thread = Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = Thread(target=send_messages, args=(client_socket,))
send_thread.start()
