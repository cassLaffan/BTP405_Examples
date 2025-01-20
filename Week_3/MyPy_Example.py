'''
Let's use mypy now! Notice we're not importing anything.
'''

# Now we have some type enforcement
def greet(name: str) -> str:
    return "Hello, " + name


# When we run this with mypy, it will give an error
if __name__ == "__main__":
	greet(5) 