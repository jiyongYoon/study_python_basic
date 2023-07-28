# 절대값
print(abs(3.1)) # 3.1
print(abs(-5)) # 5

# 전체 요소 참인지 확인
a = [1, '참', True, 1 == 1]
b = [0, '참', True]
c = [] # 얘만 all() 이나 any()에 특이하게 반응하네..?
d = [0, False, 1 == 2]

print(all(a)) # True
print(all(b)) # False
print(all(c)) # True
print(all(d)) # False

# 전체 요소 하나라도 참인지 (즉 전체 거짓일때만 False)
print(any(a)) # True
print(any(b)) # True
print(any(c)) # False
print(any(d)) # False

# 유니코드 숫자 -> 문자
print(chr(97)) # a
print(chr(44032)) # 가

# 문자 -> 유니코드 숫자
print(ord('a')) # 97
print(ord('가')) # 44032

# 객체가 지닌 함수나 변수를 보여줌
print(dir(a)) # 리스트 함수가 보임
print(dir({})) # 딕셔너리 함수가 보임
from class_test.calculator import FourCal
print(dir(FourCal())) # 'a', 'add', 'b', 'div', 'mul', 'setdata', 'sub' 이런 변수와 함수까지 나옴

# 몫과 나머지 튜플 반환
print(divmod(5, 3)) # (1, 2)

# 컬렉션 순회하면서 인덱스와 객체 리턴
for i, item in enumerate(a):
    print(i, item)

# 문자열로 구성된 표현식을 입력으로 받아 실행 결과를 리턴
print(eval('1 + 2'))
print(eval('divmod(4, 3)'))
print(eval('FourCal().add(3, 6)'))

# 필터 filter(함수, 반복_가능한_데이터)
def get_true(x):
    return x == True

print(list(filter(get_true, a))) # a를 돌면서 get_true 함수에 필터링된 요소들을 리턴한 값을 리스트에 담아서 출력해라

# 필터로 사용할 함수같은 경우는 람다로 사용해도 좋을 수 있다.
print(list(filter(lambda x: x == True, a)))


# 16진수
print(hex(14))

# 객체 참조값
print(id(a))

s = '객체 참조값'
print(id(s))
print(id('객체 참조값'))
print(id(s) == id('객체 참조값')) # True

# 사용자에게 입력을 받음
# input_value = input("입력하세요: ")
# print(f"당신이 입력한 내용은 '{input_value}' 입니다.")

# 정수로 리턴
print(int(3.5))
print(int('35')) # 이렇게 문자이지만 숫자로 치환될 수 있는 것들은 저렇게 출력 가능
print(int('11', 2)) # 2진수 11을 10진수로
print(int('1A', 16)) # 16진수 1A를 10진수로

# 입력받은 객체가 그 클래스의 인스턴스인지 판단하여 T / F 리턴
cal = FourCal()
print(isinstance(cal, FourCal)) # True
print(isinstance(a, FourCal)) # False

# 요소 개수 리턴
print(len('python'))
print(len(a))

# 반복 가능한 데이터 입력받아 리스트로 리턴
print(list('python')) # ['p', 'y', 't', 'h', 'o', 'n']
dic = {
    "name": "Yoon",
    "address": "Seongnam"
}
print(list(dic)) # ['name', 'address']
print(list(dic.keys())) # ['name', 'address']
print(list(dic.values())) # ['Yoon', 'Seongnam']


# 함수와 반복 가능한 데이터 입력받아 각 요소에 함수를 적용한 결과를 리턴 (Java Stream Map과 비슷하구만)
numList = [1, 2, 3, 4, 5]

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


print(two_times(numList))


def two_times_for_map(x):
    return x * 2


print(map(two_times_for_map, numList)) # 이러면 map object가 반환됨. <map object at 0x0000025602BD6CA0>
print(list(map(two_times_for_map, numList)))
print(list(map(lambda x: x * 2, numList)))

# 최대값, 최소값
print(max(numList))
print(max('python')) # y
print(min('python')) # h

# 정수를 8진수로 리턴
print(oct(13))

# 파일 읽기
# f = open("C://Users/black/OneDrive/바탕 화면/tttt.txt", "r") # w: 쓰기모드, r: 읽기모드, a: 추가모드, b: 바이너리 모드, 중복 가능
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()


# 제곱
print(pow(2, 4))

# 범위 값을 반복 가능한 객체로 만들어서 리턴, range([start], stop [, step])
print(list(range(5)))
print(list(range(5, 15)))
print(list(range(5, 15, 2)))

# 정렬한 데이터를 리스트로 리턴
alist = [5, 3, 7, 1, 2, 4]
blist = ['b', 'd', 'u', 't', 'y', 'm']
clist = ['python', 'java', 'go', 'kotlin']
print(sorted(alist))
print(sorted(blist))
print(sorted(clist))
clist.sort() # 리스트의 sort()는 객체 자체를 정렬함.
print(clist)

# 데이터 합 리턴
print(sum(alist))

# 반복 데이터를 튜플로
a_tuple = tuple(alist)
print(a_tuple)

# 자료형 확인
print(type(alist))
print(type(a_tuple))
print(type('python'))

# 동일한 개수로 이루어진 데이터들을 묶어서 맅턴
print(list(zip(alist, blist))) # [(5, 'b'), (3, 'd'), (7, 'u'), (1, 't'), (2, 'y'), (4, 'm')]
print(list(zip("abc", "가나다"))) # [('a', '가'), ('b', '나'), ('c', '다')]


