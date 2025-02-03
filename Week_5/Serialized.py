import threading
'''
In this file, we're taking a look at how we might avoid race conditions 
by using a lock. This means that a thread can only access one resource at 
a time. Again, smart use of functions and not using globals also ensures
this genrally.

Furthermore, the GIL as of Python 3.10 really makes getting a race
condition difficult. It locks byte values from more than one thread at
a time.
'''

# Again not a fan of the global
counter = 0

def increment(lock):
	global counter
	for _ in range(100000):
		with lock:  # Acquire the lock
			counter += 1
		# Lock is automatically released when the block ends

if __name__ == "__main__":
	lock = threading.Lock()
	threads = []
	for _ in range(4):
		thread = threading.Thread(target=increment(lock))
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()

	print(f"Final counter value: {counter}")  # Now it's 200000!