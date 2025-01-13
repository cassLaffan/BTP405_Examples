'''
Let's look at Python decorators. Again, decorators are just functions
that wrap around other functions. They don't modify the original function.
We can also wrap several decorators around a single function.
'''
# Our first decorator! Note, at this point you should understand
# that we can return functions and have function arguments.
def decorator(func):
	def wrapper():
		print("Before function")
		func()
		print("After function")
	return wrapper

def another_decorator(func):
	def wrapper():
		print("Another before function")
		func()
		print("Another after function")
	return wrapper

@decorator
@another_decorator
def a_function():
	print("Hello, world!")


# Here, let's look at decorators with arguments!
# This function merges all the functionalities we've learned this
# week into one (cursed) decorator.

# Definining our decorator, will repeat our function we've 
# wrapped n times. You'll need to wrap your decorator in
# an extra function which can take an argument.
def repeat(n):
    # our real decorator now.
    def decorator(func):
        # Our wrapper with an arbitrary iterable argument list and
        # abitrary argument names
        def wrapper(*args, **kwargs):
            # Accesses the argument from repeat, note the scope
            for _ in range(n):
                # calls our function
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    a_function()
    say_hello()