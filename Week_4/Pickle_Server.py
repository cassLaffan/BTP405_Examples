import socket
import pickle

if __name__ == "__main__":
	# the socket constructor opens a socket here with the address family
	# (a good example is AF_UNIX). INET is the most common network one.
	# TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('localhost', 8000))
	server_socket.listen(5)

	print("Server is listening...")

	try:
		# The accept function returns a new socket object and the address
		client_socket, client_address = server_socket.accept()
		print(f"Connection from {client_address}")

		# Create a Python object to send
		data_to_send = {"message": "Hello, client!", "number": 42}
		serialized_data = pickle.dumps(data_to_send)

		# Send serialized object
		client_socket.send(serialized_data)
		
		client_socket.close()
	except socket.error:
		print("No client to be found!")

	# Close the connection
	server_socket.close()
