a = []
a1 = list()
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = ['Life', 'is', 1, 2]
e = ['Life', 'is', [1, 2]]

print(a)
print(a1)

print(d[2])

print(e[2]) #[1, 2]
print(e[-1]) #[1, 2]

print(e[2][1]) #2

f = [1, [2, [3, [4, 5]]]]

print(f[1][1][1][1]) #5

print(f[0:2][1:2].__eq__(f[1:2])) #True

print(f[1]) #[2, [3. [4, 5]]]
print(f[1][1:2]) #[[3, [4, 5]]] 1번 인덱스 원소의 1번 인덱스 요소

a = [1, 2, 3]
b = [2, 3, 4]

print(a + b) #[1, 2, 3, 2, 3, 4]
print(a * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 2hi를 만들고 싶다면?
hiString = "hi"

# print(a[1] + st) #에러 TypeError: unsupported operand type(s) for +: 'int' and 'str'

# str()는 정수나 실수를 문자열로 바꾸어주는 파이썬의 내장 함수
print(str(a[1]) + hiString)

# del 함수: 객체를 삭제하는 파이썬 내장함수
list = [1, 2, 3, 4, 5]
del list[1]
print(list) #[1, 3, 4, 5]
del list[2:]
print(list) #[1, 3]

# append: 객체 추가
list.append("스트링")
print(list)

# sort: 정렬
# list.sort() #에러 not supported between instances of 'str' and 'int'
list = [1, 4, 6, 2, 5, 78, 2, 4]
list.sort()
print(list) #[1, 2, 2, 4, 4, 5, 6, 78]
print(list.sort()) # 는 None 이 나오는데, 왜 그러는지는 아직 모르겠음.
list.reverse()
print(list) #[78, 6, 5, 4, 4, 2, 2, 1]

# insert: 삽입
list.insert(0, 100)
print(list) #[100, 78, 6, 5, 4, 4, 2, 2, 1]
list.insert(len(list), 0)
print(list) #[100, 78, 6, 5, 4, 4, 2, 2, 1, 0]
list.append(0)
print(list) #[100, 78, 6, 5, 4, 4, 2, 2, 1, 0, 0]

# pop: 요소 꺼내기
popLast = list.pop() # 마지막 요소
print(popLast) #0
print(list) #[100, 78, 6, 5, 4, 4, 2, 2, 1, 0]
popFirst = list.pop(0) # 0번째 요소
print(popFirst) #100
print(list) #[78, 6, 5, 4, 4, 2, 2, 1, 0]

# count: 포함된 요소 세기
list = [1, 2, 3, 2, 1]
print(list.count(2))

# extend: 리스트 확장
list2 = [1, 3, 5, 3, 1]
list.extend(list2) # == list += list2
print(list) #[1, 2, 3, 2, 1, 1, 3, 5, 3, 1]
