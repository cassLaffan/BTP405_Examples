from typing import List

'''
Here, we have a generic Person class with type hinting!
This takes out ambguity in our code. For example, we
might not make it clear age should be an int; it could be
a float!
'''

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_details(self) -> str:
        return f"{self.name} is {self.age} years old."

def get_oldest_person(people: List[Person]) -> Person:
    # let's also re-use our knowledge from last week!
    # Lambdas are just in-line functions, useful for a
    # lot of sorting or finding built-in functions.
    return max(people, key=lambda p: p.age)
