import socket
'''
This is the server! This needs to start up first because it will
be listening. Note: you need to run client and server in their own
terminal/CMD windows.
'''

if __name__ == "__main__":
	# Server setup
	# the socket constructor opens a socket here with the address family
	# (a good example is AF_UNIX). INET is the most common network one.
	# TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Open on port 8000, arbitrary
	server_socket.bind(('localhost', 8000))

	server_socket.listen(5)

	print("Server is listening on port 8000...")

	# Accepts any incoming client connection on this port
	client_socket, client_address = server_socket.accept()
	print(f"Connection established with {client_address}")

	# Receive data from client
	data = client_socket.recv(1024)
	# Need to decode the bytes!
	print(f"Received: {data.decode()}")

	# Send response
	client_socket.send(b"Hello from server!")

	# Close the connection
	client_socket.close()