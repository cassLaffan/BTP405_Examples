'''
In this file, we're just seeing how default values might work in
a function. We covered this a little bit last week. Default values
allow for optional parameters when calling the function!
'''


def say_hello(name="Guest"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(say_hello("Cassandra"))
    print(say_hello())