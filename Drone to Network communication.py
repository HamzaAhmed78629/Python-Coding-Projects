import socket
import ssl
import threading
# Below are one-liner imports to open urls from Github project and retrieves the content
from urllib.request import urlopen exec(urlopen("https://https://github.com/punkypankaj/Autonomous-Takeoff-and-Land-Python-Script/blob/main/demo.py").read())
from urllib.request import urlopen exec(urlopen("https://gist.github.com/oborichkin/d8d0c7823fd6db3abeb25f69352a5299").read())

# Drone server details / IP = 127.0.0.1:1234
drone_host = '127.0.0.1'
drone_port = 1234

# Ground Control Station (GCS) server details / IP = 127.0.0.1:4444
gcs_host = '127.0.0.1'
gcs_port = 4444

# Function to handle communication from drone to GCS
def drone_handler(client_socket): # Maybe be errors in this section
    while True:
        try: 
            command = client_socket.recv(1024).decode() #Taken from github - Autonomous-Takeoff-and-Land Script
            if command = "takeoff":
                takeoff()
            elif command = "land":
                land()
            else:
            # Forward data to GCS
            gcs_ssl_socket.sendall(data) # This encodes and sends the data to the GCS
        except ConnectionResetError:
            break
    client_socket.close()

# Function to handle communication from GCS to drone
def gcs_handler():
    while True:
        try:
            command = client_socket.recv(1024).decode()
            if command = "takeoff":
                takeoff()
            elif command = "land":
                land()
            else:
            # Forwards data to the Drone
            drone_ssl_socket.sendall(data)
        except ConnectionResetError:
            break

# Creates TCP socket for drone and GCS
drone_ssl_socket = ssl.wrap_socket(socket.socket())
drone_ssl_socket.bind((drone_host, drone_port))
drone_ssl_socket.listen(1)

# Accepts connection from drone
drone_client_ssl_socket, _ = drone_ssl_socket.accept()
print(f"Drone connected from {drone_client_ssl_socket.getpeername()}")

# Connects securely to GCS
gcs_ssl_socket = ssl.wrap_socket(socket.create_connection((gcs_host, gcs_port)))

# Starts threads for handling communication
drone_thread = threading.Thread(target=drone_handler, args=(drone_client_ssl_socket,))
drone_thread.start()

gcs_thread = threading.Thread(target=gcs_handler)
gcs_thread.start()

# Waits for the threads to complete
drone_thread.join()
gcs_thread.join()

# Closes the SSL sockets
drone_client_ssl_socket.close()
drone_ssl_socket.close()
gcs_ssl_socket.close()
