class Family:
    lastname = '윤'

a = Family()
b = Family()

print(a.lastname) # 윤
print(b.lastname) # 윤

# 클래스 변수 -> 클래스로 만든 객체의 lastname이 모두 공유됨
Family.lastname = '최'

print(a.lastname) # 최
print(b.lastname) # 최

# 객체변수 -> a 객체의 lastname에 '박'을 할당해주면
a.lastname = '박'

print(a.lastname) # 박
print(b.lastname) # 최

# 클래스 변수 재할당
Family.lastname = '이'

print(a.lastname) # 박 -> 객체 변수로 새롭게 생성이 된 객체는 클래스 변수의 영향을 받지 않음
print(b.lastname) # 이 -> 객체 변수 할당이 아직 안된 객체는 클래스 변수 공유


## 이걸... 어따쓰지?