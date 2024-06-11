import socket

class Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = None

    def connect_to_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.server_address, self.server_port))
            print("Connected to the server.")
        except Exception as e:
            print(f"Error connecting to the server: {e}")

    def send_message_to_server(self, message):
        try:
            print("Sending to server:", message)
            self.client_socket.sendall(message.encode())
        except Exception as e:
            print(f"Error sending message to server: {e}")

    def receive_message_from_server(self):
        try:
            message = self.client_socket.recv(1024).decode()
            print("Received from server:", message)
        except Exception as e:
            print(f"Error receiving message from server: {e}")

    def close_connection(self):
        try:
            self.client_socket.close()
            print("Connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")

def main():
    client = Client("10.1.5.133", 5556)
    client.connect_to_server()

    while True:
        print("\n1. Add a book")
        print("2. Delete a book")
        print("3. Update a book")
        print("4. Display books")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            author = input("Enter the author's name: ")
            title = input("Enter the book's title: ")
            content = input("Enter the book's content: ")
            message = f"ADD:{author}:{title}:{content}"
            client.send_message_to_server(message)
            client.receive_message_from_server()
        elif choice == "2":
            title = input("Enter the title of the book to delete: ")
            message = f"DELETE:{title}"
            client.send_message_to_server(message)
            client.receive_message_from_server()
        elif choice == "3":
            title = input("Enter the title of the book to update: ")
            author = input("Enter the new author's name: ")
            content = input("Enter the new content of the book: ")
            message = f"UPDATE:{title}:{author}:{content}"
            client.send_message_to_server(message)
            client.receive_message_from_server()
        elif choice == "4":
            message = "DISPLAY"
            client.send_message_to_server(message)
            client.receive_message_from_server()
        elif choice == "5":
            client.close_connection()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
