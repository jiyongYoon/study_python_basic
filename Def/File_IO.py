# 파일 열기
f = open("새파일.txt", 'w')
# 첫 번째 인자: 파일 위치 - 아무것도 안쓰면 현재 파일 위치
# 두 번째 인자: r - 읽기 모드 / w - 쓰기 모드 / a - 추가 모드(수정)
f.close()


f = open("새파일.txt", 'w')
for i in range(1, 15):
    data = "%d번째 줄입니다.\n" % i
    # 데이터 작성
    f.write(data)
f.close()


# 파일 읽기
f = open("새파일.txt", 'r')
while True:
    readline = f.readline()
    if not readline:
        break
    else:
        readline_ = readline[:-1] # == readline.strip() : 줄 끝에 있는 줄바꿈 문자를 제거한다.
        print(readline_)
f.close()
print()

# # (번외) 입력 읽기
# while True:
#     data = input()
#     if not data: break;
#     print(data)

# 파일 읽기 2
f = open("새파일.txt", 'r')
readline = f.readlines()
for data in readline:
    data_ = data.strip()
    print(data_)
f.close()
print()

# 파일 읽기 3
f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()
print()

# 파일 읽기 4
f = open("새파일.txt", 'r')
for data in f:
    print(data.strip())
f.close()
print()

# 새로운 내용 추가하기
f = open("새파일.txt", 'a')
for i in range(15, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
print()

# 파일 읽기 4
f = open("새파일.txt", 'r')
for data in f:
    print(data.strip())
f.close()
print()

##################################

def read_file(name, type):
    f = open(name, type)
    for data in f:
        print(data.strip())
    f.close()
    print()

# 파일 열고 닫기 자동처리
with open("새파일.txt", 'a') as f:
    f.write("이 내용을 추가하자!")

read_file("새파일.txt", 'r')

# 파일 열고 닫기 자동처리
with open("새파일.txt", 'w') as f:
    f.write("이 내용으로 다 바꾸자!")

read_file("새파일.txt", 'r')

