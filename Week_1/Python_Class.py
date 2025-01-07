'''
This is an example of a Python class. Notice that we still use the class keyword,
just like in C++? However, unlike in C++, we declare our member attributes
in the constructor (declared below as __init__).
'''

class Book:
    '''
    Notice the __ in front of and after these methods? These are dunder (double under
    score) methods. These replace your classic syntax is C++ for things like operator
    overloads and constructors.
    
    Furthermore, notice "self". That's Python's representation of the current object.
    It must be the first argument in member methods!
    '''
    def __init__(self, bt=None, au=None, pd=None, pl=None):
        '''This is our Book constructor! I've given the arguments default values.'''
        self.book_title = bt
        self.author = au
        self.pub_date = pd
        self.page_length = pl
        self.current_page = 0

    def __str__(self):
        '''A string method, allows Python to parse our class objects as a string.'''
        return f"Title: {self.book_title} \nAuthor: {self.author}\n"

    def mark_page(self, pages_read):
        '''An example of a modifier member method.'''
        self.current_page += pages_read

    @property
    def peak_next_page(self):
        '''A property! Useful for when you want something to act like a member
        attribute but will not actually make changes to the state of your object.'''
        return self.current_page + 1

if __name__ == "__main__":
    # Declaring a class object in Python is similar to C++, except we don't give the
    # variable a type.
    our_first_book = Book("War and Peace", "Tolstoy", "Jan 1 1867", 600)

    print(our_first_book, end="")
    # These fs at the beginning of strings are f-strings. They allow us to format 
    # strings with variables and values.
    print(f"Our current page is: {our_first_book.current_page}")

    our_first_book.mark_page(200)

    print(f"Our current page is: {our_first_book.current_page}")

    print(f"The next page is: {our_first_book.peak_next_page}")

    print(f"Our current page is: {our_first_book.current_page}")
