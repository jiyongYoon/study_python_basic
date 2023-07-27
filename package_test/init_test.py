# import class_test # 패키지 초기화
# class_test 패키지의 __init__.py 모듈이 실행됨.

from class_test.calculator import FourCal # 이렇게 하위 모듈을 import 할때도 동일하게 초기화됨

cal = FourCal()
print(cal.add(5, 10))