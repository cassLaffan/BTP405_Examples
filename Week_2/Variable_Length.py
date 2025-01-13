'''
In this file, we'll be looking at the unpacking operator *.
When in front of a parameter in a function, it allows for a varying number
of arguments. When used in front of an iterable (such as a list
or tuple), it will just unpack it. That's useful for print statements!
'''

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")


if __name__ == "__main__":
    name_list = ["Cass", "Tav", "Craig"]
    # Let's see how * unpacks the list above
    print(*name_list)
    
	# Now, we'll see how we can treat iterables as argument lists
    greet(*name_list)