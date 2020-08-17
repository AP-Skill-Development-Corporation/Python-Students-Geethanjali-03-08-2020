class Calci:
    def power(a,b):
        return a ** b
    def sub(a,b):
        return a - b
class Calci1:
    def isEven(val):
        if val % 2 == 0:
            return True
        return False
class Calci2:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    def __add__(self):
        return self.val1 + self.val2
    def __mul__(self):
        return self.val1 * self.val2