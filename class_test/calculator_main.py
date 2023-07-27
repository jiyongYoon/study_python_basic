from calculator import FourCal, MoreFourCal, SafeFourCal

cal = FourCal(4, 7)
print(cal.a)
print(cal.b)

print(cal.add())
print(cal.add(3, 2))
print(cal.add())
print(cal.add(3, ))

cal2 = MoreFourCal(1, 55, 3)
print(cal2.a)
print(cal2.b)
print(cal2.c)
print(cal2.add())
print(cal2.add(3, 2))

cal3 = SafeFourCal()
print(cal3.classname)
