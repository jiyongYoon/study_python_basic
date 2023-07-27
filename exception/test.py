try:
    f = open("Random Name", 'r')
except: # 발생 오류를 특정하지 않음
    print('파일 열다가 에러 남')


try:
    f = open("Random Name", 'r')
except FileNotFoundError:
    print('파일을 찾을 수 없음')

try:
    f = open("Random Name", 'r')
except FileNotFoundError as e:
    print(f'파일을 찾을 수 없음, {e}')

try:
    f = open("Random Name", 'r')
except FileNotFoundError as e:
    print(f'파일을 찾을 수 없음, {e}')
finally:
    print("파일 만들어서 하세용")



try:
    a = [1, 2]
    print(a[3])
    4 / 0
except:
    print("에러발생")

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except IndexError:
    print("인덱싱 에러 발생")

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except IndexError as e:
    print(f"인덱싱 에러 발생, {e}")

try:
    a = [1, 2]
    print(a[1])
    4 / 0
except IndexError as e:
    print(f"인덱싱 에러 발생, {e}")
except ZeroDivisionError as e:
    print(f"0으로 나눌 수 없음, {e}")

try:
    a = [1, 2]
    print(a[1])
    4 / 0
except IndexError as e:
    print(f"인덱싱 에러 발생, {e}")
except ZeroDivisionError as e:
    print(f"0으로 나눌 수 없음, {e}")
finally:
    print("안녕하세용")

