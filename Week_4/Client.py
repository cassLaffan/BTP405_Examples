import socket
'''
This is the client! Start up the server first before running this file.
Note: you need to run client and server in their own terminal/CMD windows.
'''

if __name__ == "__main__":
	# Client setup
	# For explanation, see Server file
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# I've wrapped the client connection in a try/except block, just in case
	# the server isn't on!
	try:
		# Connects to server listening
		client_socket.connect(('localhost', 8000))

		# Send message to server
		client_socket.send(b"Hello from client!")

		# Receive response from server
		response = client_socket.recv(1024)
		print(f"Server says: {response.decode()}")

	except socket.error:
		print("Socket isn't listening!")

	# Close the connection
	client_socket.close()