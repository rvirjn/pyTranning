import time
from urllib import urlopen
def with_retries(retries=5, delay=0.1):
    def decor(f):
        def wrapper(*args):
            for i in range(retries):
                try:
                    print ('retry')
                    return f(*args)
                except Exception as e:
                    print ('failed')
                time.sleep(delay)
            print ('giving up')
        return wrapper
    return decor


@with_retries(retries=5, delay=0.5)
def wget(url):
    response = urlopen(url)
    if response:
        return response.read()

if __name__ == "__main__":
    #wget('http://10.165.83.226/vpn/linux/client.key')
    wget('http://www.google.com')

def debug(f):
    return f