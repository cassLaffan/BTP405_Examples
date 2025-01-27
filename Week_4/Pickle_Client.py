import socket
import pickle

'''
In this file, we unpickle the object we recieved. 
'''

if __name__ == "__main__":
	# Client setup
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('localhost', 8000))

	try:
		# Receive data
		serialized_data = client_socket.recv(1024)

		# Unpickle the data
		received_data = pickle.loads(serialized_data)
		print(f"Received data: {received_data}")
	except socket.error:
		print("Couldn't connect to server!")

	# Close the connection
	client_socket.close()
