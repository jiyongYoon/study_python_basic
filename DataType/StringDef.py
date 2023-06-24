a = "hobby"

# 문자 개수 세기
print(a.count('b'))

# 인덱스 찾기
print(a.find('o')) #1
print(a.index('o')) #1
print(a.find('k')) #-1
# print(a.index('k')) #에러

print(a.find('b')) #2
print(a.find('by')) #3
print(a.index('b')) #2
print(a.index('by')) #3

# 문자열 삽입
print('!'.join(a)) #h!o!b!b!y
print(a)

# 문자열 나누기
str = "Hello, My name is Yoon"
print(str.split())
print(str.split(" "))
print(str.split(','))

# 문자열을 변경하는(삽입, 나누기 등) 함수는 문자 자체가 변하는게 아니라 변경한 값을 리턴하는 개념임