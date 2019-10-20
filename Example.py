# Description:
# Provisioning VM via Converged blueprint
# Group-physical-st: optional
# Timeout: 2400

import unittest

__author__ = "raviranjan"


def run(values, initial=50):
    return initial +sum(values)

# variable number of Arguments
def mysum(*agrs):
    return agrs

def make_adder(*args):
    pass

def compose(f, g):
    def func(x):
        return f(g(x))
    return lambda x: f(g(x))


def zip_with(f):
    def fun(list1, list2):
        return [f(list1[i], list2[i]) for i in range(len(list1))]
    return fun


def fold(f, default=0):
    def operation(list1):
        s = default
        for item in list1:
            s = f(s, item)
        return s
    return operation


def add(x, y):
    return x+y
class Tester(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_addinner(self):
        test_add()

def test_add():
    assert add(9,8) == 17

if __name__ == "__main__":
    adder = zip_with(lambda x, y: x + y)
    multi = zip_with(lambda x, y: x * y)

   # print adder([1, 2, 3, 4], [5, 6, 7, 8])
    print fold.__name__
    sum_= fold(add, default=3)
    #print sum_([1,2,3,4])
    unittest.main()

