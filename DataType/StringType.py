print("큰따옴표")
print('작은따옴표')
print("""큰따옴표 3개""")
print('''작은따옴표 3개''')

print("이렇게 ' 작은 따옴표 추가")
print('이렇게 \' 작은 따옴표 추가')
print('이렇게 " 큰 따옴표 추가')
print('이렇게 \" 큰 따옴표 추가')

# 문자열을 더하면 추가하고 곱하면 반복 반복 반복
print('문자열을 더하면' + ' 추가하고 곱하면' + ' 반복' * 3)

a = "문자열 길이는 len()으로"
print(len(a))

print(a[4:6])
print(a[-11:-9])
print(a[4:6].__eq__(a[-11:-9]))

# 문자열 포매팅
str = 'I eat %s.' % 'apple'
print(str)

str = 'I eat %d %s.' % (3, 'apples')
print(str)

str = 'I eat {0} apples.'.format(3)
print(str)

str = 'I eat {0} {1}.'.format(3, 'apples')
print(str)

str = 'I eat {0} {1} {0} times.'.format(3, 'apples')
print(str)

str = 'I eat {3} apples.'
print(str)

str = 'I eat {{3}} apples.'.format()
print(str)

