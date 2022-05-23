

class DefaultException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return 'DefaultException, {0}'.format(self.message)
        else:
            return 'DefaultException'

class DividingByZero(DefaultException):
    def __str__(self):
        if self.message:
            return 'Dividing by Zero, {0}'.format(self.message)
        else:
            return 'Dividing by Zero'

class Overflow(DefaultException):
    def __str__(self):
        if self.message:
            return 'Overflow, {0}'.format(self.message)
        else:
            return 'Overflow'


class int_16:
    def __init__(self, value):
        self.max = 32767
        self.min = -32768
        if value <= self.max and value >= self.min:
            self.value = value
        else:
            raise Overflow
    
    def __add__(self, other):
        sum = self.value + other.value
        return int_16(sum)
    
    def __sub__(self, other):
        sub = self.value - other.value
        return int_16(sub)
    
    def __mul__(self, other):
        mul = self.value * other.value
        return int_16(mul)

    def __floordiv__(self, other):
        if other.value == 0:
            raise DividingByZero
        else:
            return int_16(self.value // other.value)

    def __mod__(self, other):
        if other.value == 0:
            raise DividingByZero
        else:
            return int_16(self.value % other.value)
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value

def factor(num):
    
    if num == int_16(0):
        return int_16(1)
    else:
        return num * factor(num-int_16(1))


if __name__ == '__main__':
    A = int_16(100)
    B = int_16(2)
        #print(A%B)

    print((A*B).value)
    try:
        print(factor(A).value)
    except Exception as e:
        print(e)


