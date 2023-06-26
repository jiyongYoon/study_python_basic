s1 = set([1, 2, 3])
print(s1)

s2 = set([1, 2, 2, 3, 3, 3])
print(s2)

print(s1.__eq__(s2)) #True

s3 = set("Hello")
print(s3)

s4 = set(["Hello"])
print(s4)

print(s3.__eq__(s4)) #False

# print(s1[0]) #에러 TypeError: 'set' object is not subscriptable - 집합 자료형은 인덱스로 직접 접근 불가
list = list(s1)
print(list[0])

#####

s5 = set([1, 2, 3, 4])
s6 = set([3, 4, 5, 6])

# 교집합
print(s5 & s6)

# 합집합
print(s5 | s6)
print(s5.union(s6))

# 차집합
print(s5 - s6)
print(s5.difference(s6))

# 요소 추가
s5.add(7)
print(s5)

s5.update([8, 9, 10])
print(s5)

# 요소 제거
s5.remove(10)
print(s5)