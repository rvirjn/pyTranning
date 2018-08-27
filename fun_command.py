import sys

commands = {}

def command(f):
    commands[f.__name__] = f
    return f

def with_retries(retries=5, delay=0.1):
    pass

@with_retries(retries=5, delay=0.1)
def wget(url):
    pass


def main():
    cmdname = sys.argv[1]
    args = sys.argv[2:]
    if cmdname == 'Help':
        for fun in commands.keys():
            print ('{} = {}'.format(commands[fun].__name__ , commands[
                fun].__doc__.strip()))
    else:
        print ('Else block')
        cmd = commands[cmdname]
        cmd(*args)



@command
def cat(filename):
    """
    prints given file to standard output
    """
    print(open(filename).read())


@command
def head(filename, n):
    """
    prints first n lines from given file to standard output
    """
    with open(filename) as f:
        for i in range(n):
            print(f.readline())

@command
def grep(pattern, filename):
    """
    looks for pattern in given file
    """
    for line in open(filename):
        if pattern in line:
            print(line.strip())

if __name__ == "__main__":
    main()