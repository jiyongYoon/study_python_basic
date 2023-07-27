from ..method_type.language import * # 부모 디렉토리로부터 접근하여 import

class Cookie:
    pass
    # pass는 아무것도 수행하지 않는 문법으로, 임시 코드를 작성할 때 주로 사용한다.


if __name__ == '__main__':
    a = Cookie()

    print(a.__sizeof__())
    print(type(a))

    basic_lang = Language()
