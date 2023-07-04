import sys

# 파이썬 라이브러리가 설치되어 있는 디렉터리 목록 보기
print(sys.path)

# path에 모듈 추가하기
# sys.path.append("C:/~~~/~~~")
sys.path.append('C:/Users/Yoon jiyong/Desktop/develop/python/study/module')
print(sys.path)


# sys.path에 추가한 위치에 있는 모듈 사용하기
import module.mod2

a = module.mod2.add(3, 5)
print(a)



from module.mod1 import *

a = sub(3, 2)
print(a)