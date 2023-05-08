# concepts for python decorators
# src: https://youtu.be/FXUUSfJO_J4
# class

# use cases:
# executed time decorator
# debug decorator
# check decorator
# register like plugins
# cache

class CountCalls:
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi")
    
say_hi()
say_hi()