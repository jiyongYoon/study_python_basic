class Bird:

    # 상속받는 모듈에서 구현하지 않는 경우 에러가 나도록
    def fly(self):
        raise NotImplementedError
