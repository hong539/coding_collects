import functools

def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        print("Start")
        result = func(*args, ** kwargs)        
        print("End")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signatue = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signatue})")
        result = func(*args, ** kwargs)
        print(f"{func.__name__!r} returned {result!r} ")
        return result
    return wrapper
    
@debug
@start_end_decorator
def say_hi(name):
    hi = f'Hi {name}'
    print(hi)
    return hi

say_hi("Joe")