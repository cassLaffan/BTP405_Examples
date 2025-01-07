import Python_Class

'''In this file, we're taking a look at how inheritance is done by Python.
Note how we imported our file containing our book class.'''

class Manga(Python_Class.Book):
    def __init__(self, is_colour=False, bt=None, au=None, pd=None, pl=None):
        '''
    	Super is the parent class, book!
        We are invoking the parent constructor and the book parent class
        becomes the "self" in this explicit invocation of this constructor
        '''
        super().__init__(bt, au, pd, pl)
        self.in_colour = is_colour

    def __str__(self):  
        '''Another string implementation. We call the parent's string method first.'''
        return super().__str__() + f"Is it in colour? {self.in_colour}"

    def has_anime(self, sales):
        '''A method unique to Manga.'''
        return sales > 1000000

if __name__ == "__main__":
    our_manga = Manga(True, "Tomie", "Junji Ito", "June 1 2008", 200)

    print(our_manga)

    print(our_manga.has_anime(2000000))