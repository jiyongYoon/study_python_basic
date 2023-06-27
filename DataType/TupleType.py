# 리스트와 비슷하지만, 요솟값을 바꿀 수 없는 특징을 가짐

t1 = ()
t2 = (1, ) # 원소가 1개일때는 쉼표를 반드시 붙여주어야 함
t3 = (1, 2, 3)
t4 = (1, (2, 3), 4)
t5 = 1, 2, 3, 4, 5 # 튜플 생성 시 괄호 생략 가능
print(t5)
# t5[1] = 3 #에러 'tuple' object does not support item assignment

# del t2[1] #에러 'tuple' object doesn't support item deletion

