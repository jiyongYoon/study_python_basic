a = True
b = False

list = ['a', 'b', 'c', 'd']

for item in list:
    print(item)

# 리스트에 값이 있으면 True, 없으면 False로 인식하여 조건문 자리에 사용될 수 있다.
if list:
    print("참") #참
else:
    print("거짓")

print(bool(list)) #True

while list:
    print(list.pop())

if list:
    print("참")
else:
    print("거짓") #거짓

print(bool(list)) #False
