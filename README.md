# File Transfer Application
Follow the instructions below to get started.

### Prerequisites
Make sure you have Python installed on your system before proceeding.

---

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
---
You have now successfully transferred a file using the File Transfer Application!