import socket
import ssl

def start_server(port):
    """Start the TLS-enabled file transfer server."""
    assert 1024 <= port <= 65535, "Port number should be between 1024 and 65535."

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f"TLS-enabled server listening on port {port}...")

    # Create SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(
        certfile='C:\\Users\\Mohamed Yusuf\\OneDrive\\Desktop\\NetFileXfer\\server\\cert.pem', 
        keyfile='C:\\Users\\Mohamed Yusuf\\OneDrive\\Desktop\\NetFileXfer\\server\\key.pem')

    while True:
        client_socket, client_address = server_socket.accept()
        secure_socket = context.wrap_socket(client_socket, server_side=True)
        print(f"Accepted secure connection from {client_address}")

        try:
            file_name_length = int.from_bytes(secure_socket.recv(4), byteorder='big')
            file_name = secure_socket.recv(file_name_length).decode()
            print(f"Receiving file named: {file_name}\n" + "*" * 80)

            with open(file_name, 'wb') as file:
                while True:
                    data = secure_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)

            print(f"Received file {file_name}")

        except Exception as e:
            print(f"Error: {e}")

        secure_socket.close()
        print(f"Connection with {client_address} closed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: server.py <PORT>")
        sys.exit(1)

    try:
        port = int(sys.argv[1])
        start_server(port)
    except ValueError:
        print("Port should be a number.")
