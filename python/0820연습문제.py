def is_odd(a):
    if a % 2==0:
        return "짝수입니다"
    else:
        return "홀수입니다"

print(is_odd(2))
# print(is_odd(3))


def average(*args):
    avg = sum(args) / len(args)
    return avg

avg = average(1,2,3,4,5)
print(avg)


class Calculator:
    def __init__(self):
        self.value = 0
    def add(self,val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
        return self.value

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
            return self.value
        else:
            return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)