# A Decorator is a function that modifies or extends the behavior of another function without changing its original code.
# Decorator Example
def my_decorator(func):
    def wrapper():
        print("**********")
        print("Before Function Execution")
        
        func()
        
        print("After Function Execution")
        print("**********")
    return wrapper

@my_decorator
def greet():
    print("Welcome to Python Decorators!")

greet()