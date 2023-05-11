import daemon

def do_something():
    while True:
        # Do something here
        pass

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == '__main__':
    run()