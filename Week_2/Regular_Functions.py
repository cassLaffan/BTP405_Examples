'''
This file has a few examples of just regular functions, including
positional arguments, etc.
'''

def subtract(a, b):
	return a - b

def multiply(a, b):
    return a * b


if __name__ == "__main__":
	# Note the order of arguments. a - b
	subtract(10, 5)
	# When using keyword arguments, we can actually flip their order
	multiply(b=10, a=5)
