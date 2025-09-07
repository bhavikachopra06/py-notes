# simple function (no parameters)
def greet():
    print("Hello, World!")
greet()

# function with parameter
def greet(name):
    print(f"Hello, {name}")
greet("Chaitanya")

# function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}")
greet()  # uses default value
greet("Bhavika")  # overrides default

# function with multiple parameters
def info(name, age):
    print(f"Name: {name}, Age: {age}")
info("Chaitanya", 21)  # positional arguments
info(age=20, name="Bhavika")  # keyword arguments

# function with *args and **kwargs
def func(*args, **kwargs):
    print(args)    # tuple of positional arguments
    print(kwargs)  # dictionary of keyword arguments
func(1, 2, 3, name="Chaitanya", age=21)

# nested function
def outer():
    x = 10
    def inner():
        print(x)  # inner function uses outer variable
    inner()
outer()

# global variable usage
x = 5
def func():
    global x
    x = 10
    print(x)  # prints 10 (inside function)
func()
print(x)  # prints 10 (global changed)

# docstring example
def desc():
    """This function prints a description message."""
    print("This is a sample function.")
desc()
print(desc.__doc__)  # prints docstring

# lambda function (anonymous function)
square = lambda x: x * x
print(square(5))  # prints 25
