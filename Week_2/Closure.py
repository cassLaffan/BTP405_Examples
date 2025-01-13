'''
Here, we'll be looking at the syntax for closures. Note, you should come
into this file with an understanding of scope. If you aren't too sure about
scope and functions as arguments, return values, etc., go read the other 
examples in this folder first.
'''
# Similar function from other files
def outer(x):
	def inner(y):
		return x + y
	return inner

if __name__ == "__main__":
	closure_function = outer(10)
	print(closure_function(5))
