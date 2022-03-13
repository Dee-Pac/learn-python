from typing import Type


class Fibonacci:

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def fib(self, num, d = dict()):

        if num in d:
            return d[num]

        if (num <=1):
            d[num] = num
            return d[num]
        
        d[num] = self.fib(num-1, d) + self.fib(num-2, d)
        return d[num]

    def calculate(self, num):

        if not isinstance(num, int):
            raise TypeError("Incorrect input type", type(num))

        self.result = self.fib(num)
        return self.result





