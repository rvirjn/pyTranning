def make_logger(prefix):
    def print1(*args):
        print()
        print(args[0])

    return print1



if __name__ == "__main__":
    info = make_logger("[INFO]")
    warn = make_logger("[WARNING]")
    info("called some function", "ravi")

def print1():
    pass