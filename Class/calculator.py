class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal2.add(4))
print(cal1.add(7))
print(cal2.add(6))

class FourCal:
    def __init__(self):
        self.a = 0
        self.b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    ### 생성자가 이렇게 2개 이상 있으면, 제일 마지막에 있는게 적용이 되는구나.....
    ### 어떻게 하면 java처럼 여러가지 생성자를 쓸 수 있는지 나중에 알아보자

    def setdata(self, a, b):
        self.a = a # 객체변수 또는 속성
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b


# cal3 = FourCal()
#
# cal3.setdata(6, 2)
# # FourCal.setdata(cal, 6, 2) 이렇게도 사용할수는 있다.
# print(cal3.add())
# print(cal3.mul())
# print(cal3.sub())
# print(cal3.div())

cal4 = FourCal(5, 5)

print(cal4.add())
print(cal4.mul())
print(cal4.sub())
print(cal4.div())

print(type(cal1))
print(type(cal2))
# print(type(cal3))
print(type(cal4))


# 클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        return self.a ** self.b

c = MoreFourCal(10, 2)
print(c.add())
print(c.pow())


# 클래스 상속 및 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.b == 0:
            return 0
        else:
            return self.a / self.b

cal5 = SafeFourCal(4, 0)
print(cal5.div())

