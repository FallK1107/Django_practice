def add(a, b):
    result = a+b
    return result

result = add(7,3)
print(result)


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3)
print(result)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i     
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# a = 3
# b = 4
# print(add(a,b))


def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3, 4)



class FourCal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def setData(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        result = self.a+self.b
        return result
    def mul(self):
        result = self.a*self.b
        return result
    def sub(self):
        result = self.a-self.b
        return result
    def div(self):
        result = self.a/self.b
        return result

a = FourCal(4,2)
# a.setData(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# a = MoreFourCal(4, 2)
# print(a.pow())


class SafeFourCal(FourCal):
    def div(self):
        if self.b == 0:
            return 0
        else:
            return self.a / self.b

c = SafeFourCal(4, 0)
print(c.div())