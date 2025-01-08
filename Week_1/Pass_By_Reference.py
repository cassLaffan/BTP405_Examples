'''
In this file, we're exploring the behaviour of variables in Python.
Every function is pass-by-reference in Python; however, immutable
types (such as numeric types) behave like "pass-by-value".
'''

def modify_values(immutable_value, mutable_value):
    # Immutable types (e.g., integers or strings) behave like pass-by-value
    immutable_value += 5
    print(f"Inside function, modified immutable_value: {immutable_value}")

    # Mutable types (e.g., lists) behave like pass-by-reference
    mutable_value.append(10)
    print(f"Inside function, modified mutable_value: {mutable_value}")
    return immutable_value

if __name__ == "__main__":
	# Test the function with both an immutable and a mutable type
	x = 5                # Immutable type (integer)
	y = [1, [2, 3], "apple"]        # Mutable type (list)

	print(f"Before function call: x = {x}, y = {y}")

	modify_values(x, y)

	print(f"After function call: x = {x}, y = {y}")
