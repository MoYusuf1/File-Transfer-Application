import socket
import ssl
import sys
import os

def send_file(server_ip, server_port, file_path):
    """Send a file to the TLS-enabled server."""
    assert os.path.exists(file_path), "File not found."

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set up SSL context
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # For self-signed certificates

    secure_socket = context.wrap_socket(client_socket, server_hostname=server_ip)

    try:
        secure_socket.connect((server_ip, server_port))
        print(f"Securely connected to server at {server_ip}:{server_port}")

        file_name = file_path.split('/')[-1]
        secure_socket.send(len(file_name.encode()).to_bytes(4, byteorder='big'))
        secure_socket.send(file_name.encode())

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                secure_socket.send(data)

        print("File sent successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        secure_socket.close()
        print(f"Secure connection to {server_ip}:{server_port} closed.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: client.py <SERVER_IP> <SERVER_PORT> <FILE_PATH>")
        sys.exit(1)

    server_ip = sys.argv[1]

    try:
        server_port = int(sys.argv[2])
        assert 1024 <= server_port <= 65535, "Port number should be between 1024 and 65535."
        file_path = sys.argv[3]
        send_file(server_ip, server_port, file_path)
    except ValueError:
        print("Port should be a number.")
