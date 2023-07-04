def add(a, b):
    return a + b

def sub(a, b):
    return a - b


print(__name__) # __main__

# __name__은 파이썬이 내부적으로 사용하는 변수.
# 직접 본인의 파일 안에서 실행을 하게 되면 __name__변수에는 __main__이 저장된다.
# 만약 해당 파일을 다른곳에서 모듈로 사용하는 경우, __name__ 변수에는 모듈 파일의 이름인 mod1이 저장된다.
if __name__ == "__main__":
    print(add(3, 5))
    print(sub(5, 1))




