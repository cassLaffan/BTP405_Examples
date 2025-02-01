import threading
import time

'''
In this file, we take a look at threading in python!
Remember, threads are a lightweight sub-unit of a process.
These share memory with other threads in the same process!

Remember: A process is an active program, while a thread
is a sequence of instructions that runs within a process.
'''

def download_file(file_name):
	print(f"Downloading {file_name}...")
	# Simulate download time
	time.sleep(5)
	print(f"Finished downloading {file_name}")

if __name__ == "__main__":
	# Create threads
	threads = []
	files = ["file1.zip", "file2.zip", "file3.zip"]

	for file in files:
		thread = threading.Thread(target=download_file, args=(file,))
		threads.append(thread)
		thread.start()

	# Wait for all threads to finish
	for thread in threads:
		thread.join()

	print("All downloads complete!")