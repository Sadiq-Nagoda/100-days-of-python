# * Unlimited Positional Arguments     ARGS
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1,2,3,4,5,6,7,8,9,))
        
# ** Unlimited Keyword Arguments   KWARGS


def calculate(n,**kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=2, multiply=5, subtract=10)


class Car:
    def __init__(self, **kw):
        self.name = kw.get("name")
        self.age = kw.get("age")

My_info = Car(name = "Sadiq Usman Nagoda", age = 18)
print(My_info.name)