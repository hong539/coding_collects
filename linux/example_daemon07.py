import os
import sys

def do_something():
    while True:
        # Do something here
        pass

def run():
    fpid = os.fork()
    if fpid != 0:
        sys.exit(0)
    else:
        do_something()

if __name__ == '__main__':
    run()