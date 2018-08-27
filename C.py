def count_down(n):
    # for i in range(n, 1):
    #     print("Computing down of ", i)
    #     yield n-1
    #     print("back after yield")
    # print("Finished count down")
    while (n>1):
        yield n-1
        n = n-1
        return
def cdown(n):
    return (n-i for i in range(n))

def consumedup(items=[3,5,3,4,5,6,7,8,8,9]):
    result = []
    for i in items:
        if i not in result:
            yield i
            result.append(i)

def triangluar(n):
    sum = 0
    for i in range(1, n):
        sum = sum+i
        yield sum

if __name__ == "__main__":
    #count_down(10)
    result = count_down(8)
    # for item in result:
    #     print item
    # for item in triangluar(8):
    #     print item
    print count_down(10)
    # for item in cdown(10):
    #     print 'hi'
    #     print item