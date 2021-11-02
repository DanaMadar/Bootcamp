# # ex1
# class Test:
#     def __abs__(self):
#         '''The abs() function returns the absolute value of the given number.\
#              If the number is a complex number, abs() returns its magnitude.'''

#     def __int__(self):
#         '''The int() function converts the specified value into an integer number.\
#         The int() function returns an integer object constructed from a number or string x,\
#         or return 0 if no arguments are given. Version: (Python 3.2.5) Syntax: int(x=0) int(x, base=10)'''

#     def __input__(self):
#         '''return "member of Test"'''


# ex2
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + int(other)
        else:
            raise Exception(
                "Cannot add between Currency type <dollar> and <shekel>")

    def __iadd__(self, other):
        return self.amount + int(self.other)


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
print(c1 += 5)
print(c1 += c2)
print(c1 + c3)
