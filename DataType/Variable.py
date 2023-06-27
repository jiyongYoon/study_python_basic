list = ['a', 'b', 'c', 'd']

print(id(list)) #객체 주소 출력

# 참조값 복사, 즉 얕은 복사
list2 = list
print(id(list2))
print(list is list2) #True

a1 = [1, 2, 3]

# 얕은 복사
a2 = a1
a1[0] = 0
print('a1 = ' + str(a1)) #a1 = [0, 2, 3]
print('a2 = ' + str(a2)) #a2 = [0, 2, 3]

while a1:
    a1.pop()

print('a1 = ' + str(a1)) #a1 = []
print('a2 = ' + str(a2)) #a2 = []

# 깊은 복사
list2 = list[:]

print(id(list) == id(list2)) #False

while list:
    list.pop()

print(len(list) == 0) #True
print(len(list2) == 0) #False

# copy 모듈 이용
from copy import copy

a = [1, 2, 3]
b = copy(a)

print(id(a) == id(b)) #False
print(a is b) #False -> is 는 Java의 Object.equals와 동일하구만. 참조값 비교

#######################

# 변수 생성
a = 1
b, c = (1, 2)
print(b)
(d, e) = 3, 4
print(d)

[main, sub] = ['python', 'java']
[main, sub] = 'python', 'java' # 둘 다 동일

# 변수 동시 할당
main = sub = 'python'
print(main)
print(sub)
print(main is sub) #True
main = 'java'
print(main is sub) #False -> python 도 java 처럼 String은 값으로 할당하는가보구만

