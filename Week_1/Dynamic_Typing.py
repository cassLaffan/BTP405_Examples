'''
In this file, we're just going to play around with Python syntax and typing.
Notice the the dunder lines on line 10? That's Python's version of a main.
It's just necessary for your program to run, but generally considered good practice.
'''

# Just a python function!
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
	# Dynamic typing in action
	x = 10   # x is an int
	x = "Hello"   # x is now a string
      
	print(add_numbers(10, 20))  # Works fine
	print(add_numbers("Hello", 20))  # Runtime error: TypeError
