# concepts for python decorators
# src: https://youtu.be/FXUUSfJO_J4
# function
import functools

def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        print("Start")
        result = func(*args, ** kwargs)        
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

# print_name = start_end_decorator(print_name)

result = add5(10)
# print(help(add5))
print(add5.__name__)