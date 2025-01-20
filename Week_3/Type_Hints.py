from typing import List, Tuple
'''
In this file, we look at type hints using the typing library.
'''

# Function with type hints, where we tell Python
# what types we want to "enforce" as arguments and return
# types. Really, it's just documentation you hope other
# programmers follow.
def add_numbers(a: int, b: int) -> int:
	return a + b

# Using lists and tuples with type hints. Similar to above,
# we have type hints within Lists and Tuples, syntax defined
# in the typing module.
def process_items(items: List[str]) -> Tuple[int, str]:
	return len(items), items[0]

if __name__ == "__main__":
	# This works just fine!
	print(add_numbers(3, 4))
    
	# This does too (but goes against our documentation)
	print(add_numbers("apple", "banana"))
    
	a_list = ["Apple", "Banana", "Corn"]
	b_list = [1, 2, 3]
    
	# This works as expected
	print(process_items(a_list))

	# But do does this
	print(process_items(b_list))

