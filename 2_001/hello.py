languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

def pr():
    print(str)

str = '한국'
print(str)
str += ' 한국'
print(str)
str += ' 3'
print(str)

a = 4
if a > 3:
    print('ok')
else:
    print('no')

list = [1, 2, 3, 4]

for item in list:
    print(item)

print(sum(list))

minus = -3

plus = 5

print(sum([minus, plus]))

a = 3.4

print(sum([minus, plus, a]))

five = 5
three = 3

print(five / three)
print(five // three)
print(five % three)


str = """따옴표 3개로 감싸도 된다고?"""
pr()

str = "이렇게 내'것이야 라고 따옴표 안에 따옴표를 표현할때 쓴다고?"
pr()

str = '이렇게 내"것이야 라고 따옴표 안에 따옴표를 표현할때 쓴다고?'
pr()

str = "그냥 \"역슬레시\"를 사용하겠다 나는"
pr()

str = """줄바꿈은 어떻게 한다고? 
이렇게 한다고?"""
pr()

str = "이렇게도 되기는 한다. \n" \
      "나는 자바인"
pr()
print(len(str))
print(str[2])
print(str[-2])
print(str[-3:-1])
print(str[-3:])
print(str[3:-6])

str = "20230624 나는 파이썬 공부중이다"

i = 0
splitInt = 0
while i < len(str):
    if str[i] == '나':
        splitInt = i
        break
    else:
        i = i + 1

print(str[:splitInt])
print(str[splitInt:])

str = '20230624 나는 자바인이다.'

i = 0
startInt = 0
endInt = 0
pythonStr = '파이썬'

while i < len(str):
    if str[i:i + 2].__eq__('자바'):
        startInt = i
        endInt = i + 2
        break
    else:
        i = i + 1

print(str)
print(str[:startInt] + pythonStr + str[endInt:])



