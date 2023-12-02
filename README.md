# File Transfer Application
This implementation provides a hands-on experience with TLS, showcasing how it can be used to secure a simple file transfer application. It demonstrates the key concepts of network security, including secure socket creation, certificate-based encryption, and secure data transmission.

### Overview of the TLS-Enabled File Transfer Application

**1. Application Structure**
   - **NetFileXferServer.py**: The server script, responsible for accepting incoming file transfers.
   - **NetFileXferClient.py**: The client script, used to send files to the server.
   - **File Examples**: `mountain-lake.jpg` and `test.txt` for testing file transfers.

**2. TLS Integration for Secure Communication**
   - **TLS (Transport Layer Security)**: Adds a layer of encryption to the data being transferred, ensuring secure communication between client and server.
   - **SSL Context**: Configured in both the server and client scripts to enable TLS.
   - **Certificate and Key**: A self-signed certificate (`cert.pem`) and private key (`key.pem`) are used to establish a secure TLS connection.

**3. Server Implementation (NetFileXferServer.py)**
   - **Listening for Connections**: The server listens on a specified port for incoming connections.
   - **TLS-Enabled Socket**: When a client connects, the server socket is wrapped in an SSL context, creating a secure TLS connection.
   - **File Reception**: The server receives the file name and content securely over the TLS connection and saves the file locally.

**4. Client Implementation (NetFileXferClient.py)**
   - **Establishing a Connection**: The client establishes a connection to the server's IP and port.
   - **TLS-Enabled Socket**: The connection is secured using TLS through SSL context.
   - **File Sending**: The client sends the file name and then the file content securely to the server.

**5. Security and Encryption**
   - **Data Encryption**: All data transferred (file names and content) is encrypted using TLS, ensuring security against eavesdropping.
   - **Self-Signed Certificates**: Used for encryption in this application, suitable for testing and learning but not recommended for real-world applications.

**6. Testing and Verification**
   - **Running the Server and Client**: The server is started first, followed by the client which sends a file.
   - **File Transfer**: Files are transferred from the client to the server securely.
   - **Verification**: Successful transfer can be verified by checking the received files in the server's directory.


# Instructions

Make sure you have Python installed on your system before proceeding.
1. First run the Server
    1. Open a terminal and navigate to the directory containing NetFileXferServer.py. 
    2. Run the server script with the following command: 
    ```python NetFileXferServer.py 12000```
        * Replace 12000 with your desired port number.

2. Second run the Client
    1. Open another terminal and navigate to the directory containing NetFileXferClient.py.
    2. Run the client script to send a file to the server:
  ``` python NetFileXferClient.py localhost 12000 /path/to/file```
        * Replace /path/to/file with the actual path to the file you want to transfer, such as mountain-lake.jpg or test.txt.

* Lastly verify file transfer
  * After running the client script, check the server's directory to see if the file has been received correctly.

