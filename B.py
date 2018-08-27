import time
from urllib import urlopen
def with_retries(retries=5):
    def decor(f):
        def wrapper(*args):
            for i in range(retries):
                try:
                    return f(*args)
                except Exception as e:
                    print ('failed')
            print ('giving up')
        return wrapper
    return decor


@with_retries(retries=5)
def add(a, b):
    print a+b
    return a+b

if __name__ == "__main__":
    #wget('http://10.165.83.226/vpn/linux/client.key')
    add(3, 5)

def debug(f):
    return f