'''
In this file we look at duck typing! Python sniffs out
what type something is at runtime. But be careful! This
can lead to errors while the program is running!
'''

# Just like in Nominal_Typing.cpp, let's just make an
# add function
def add(a, b):
	return a + b

if __name__ == "__main__":
	# Works fine, returns 5
	print(add(2, 3))

	# Works fine, returns 'helloworld'
	print(add("hello", "world"))

	# Now, the following function call gives us a TypeError
	# add(2, "hello")