import socket
'''
This is the server! This needs to start up first because it will
be listening. Note: you need to run client and server in their own
terminal/CMD windows.
'''

if __name__ == "__main__":
	# Server setup
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('localhost', 8000))
	server_socket.listen(5)

	print("Server is listening on port 8000...")

	# Accept client connection
	client_socket, client_address = server_socket.accept()
	print(f"Connection established with {client_address}")

	# Receive data from client
	data = client_socket.recv(1024)
	print(f"Received: {data.decode()}")

	# Send response
	client_socket.send(b"Hello from server!")

	# Close the connection
	client_socket.close()