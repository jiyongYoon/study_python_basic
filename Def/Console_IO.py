# 키보드로 입력받아서 a에 저장
a = input()
print(a)

a = input("아무거나 입력하세요: ")
print(a)

# 아래 셋은 동일
print("life is cool")
print("life", "is", "cool")
print("life" + " is" + " cool")


word = [1, 2, 3, 4, 5]

#############################
for i in word:
    print(i) # == print(i, end='\n')

# 1
# 2
# 3
# 4
# 5
#############################
for i in word:
    print(i, end=' ')

# 1 2 3 4 5

