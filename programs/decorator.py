

def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@decorator #greet=decorator(greet)
def greet():
    print("middle")
greet()
