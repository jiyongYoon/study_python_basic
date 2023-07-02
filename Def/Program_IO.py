## type: 파일 이름을 인수로 받아 해당 파일의 내용을 출력해주는 명령프롬프트 명령어

## sys 모듈 사용

import sys

## 입력 받는 argv의 인자 중 첫 버내 인자는 파일명이 되고, 인덱스 1 이후부터 argv의 요소가 된다.
args = sys.argv[1:]
for i in args:
    print(i)

## 이 파일을 실행하고 인자를 입력받으면, 이 후 인자들을 출력하는 기능을 사용할 수 있게 된다.
## python Program_IO.py 111 222 333

for i in args:
    print(i.upper(), end=" ")