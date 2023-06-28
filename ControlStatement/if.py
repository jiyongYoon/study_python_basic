money = True

if money:
    print("택시타기")
else:
    print("걸어가기")

money = 2000

if money >= 3000:
    print("택시타기")
else:
    print("걸어가기")


time = 23
if time > 22 and money >= 3000:
    print("택시타기")
else:
    print("걸어가기")

if time >= 23 or money >= 3000:
    print("택시타기")
else:
    print("걸어가기")

type = ['water', 'fire', 'air', 'thunder']

if 'earth' in type:
    print("존재하는 타입")
else:
    print("잘못된 타입")

str = 'python'

if 't' in str:
    print("존재")
else:
    print("안존재")

print("-" * 50)

station1 = ['버스', '자전거', '기차']
print("정류장에 있는 것들")
for v in station1:
    print(v)
print("-" * 50)

if '택시' in station1:
    pass
else:
    print("카카오 택시를 부른다")

print("택시를 탄다")
print("-" * 50)

station2 = ['택시', '자전거', '기차']
print("정류장에 있는 것들")
for v in station2:
    print(v)
print("-" * 50)

if '택시' in station2:
    pass
else:
    print("카카오 택시를 부른다")

print("택시를 탄다")

print("-" * 50)
country = "대한민국"

message = "군입대 해야함" if country == "대한민국" else "군입대 안할수도 있음"

print(message)

a = "길다" if len(station1) > 3 else "짧다"
print(a)