from typing import List

a = 5
b = ""
class A:
    def __init__(self):
        self._something = "Hello"
        self._someOtherThing = "HHH"
        self._my_dict = {}
        self._private = []
        self.a = A()
        self._private.append(4)
        self.a._private.append(5)

    def method(self):
        """Some docstrings"""
        pass


class B(A):
    def method(self):
        global a
        pass

    def method2(self, arg1: str, arg2, arg3, arg4, arg5):
        """
        short desc
        Parameters:
            arg1: Some arg
            arg2 (str): Another arg
            arg3: Another
            arg4: Ohter
        """

def func(test: str, argumentCamel, A: List[int]):
    someVariable = "A"
    Another = "B"
    _HeHe = "C"
    for badName in range(3):
        print()
    global b

def camelCase(test_):
    pass

a = 1
X = 2
some_list = []
my_dict = {}
my_dictionary = {"a": 3}
instance = A()
A.method(instance)  # instance.method()
instance._private.append(3)
instance._private = []
instance.a._private.append(1)
if True:
    with open("a"):
        while True:
            for i in range(10):
                try:
                    if True:
                        pass
                except:
                    pass
                finally:
                    pass

elif True:
    pass
elif True:
    pass
elif True:
    pass
elif True:
    pass
elif True:
    pass
elif True:
    pass
elif True:
    pass
elif True:
    pass
else: pass


for x in range(10):
    print(x)

for i in range(10):
    print(i)

if True:
    pass
elif True:
    pass

if True:
    pass
else:
    if True:
        pass