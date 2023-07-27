# from class_test.method_type import *
#
# lang = language.Language()

"""
Traceback (most recent call last):
  File "D:\dev_yoon\py\study_python_basic\package_test\init_test2.py", line 3, in <module>
    language = Language()
NameError: name 'Language' is not defined

패키지 아래에 하위패키지가 있는 경우, *로 import를 하게 되면 language를 쓸 수 있을것 같지만, 그러지 못함.
__init__.py 파일에 __all__ 변수에 아래처럼 import 할 모듈을 정의 해주어야 사용할 수 있음.

# class_test.method_type.__init__.py
__all__ = ['language']
"""

from class_test.method_type import *

basic_lang = language.Language()
korean = language.KoreanLanguage()

"""
만약 from 마지막에 특정되는 것이 모듈이라면 import * 하게 되면 해당 모듈의 모든 클래스 및 함수가 import 되는게 맞음.
ex)
from class_test.method_type.langauge import *
"""

