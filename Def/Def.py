def add(a, b):
    return a + b


def add_no_return(a, b):
    a + b


print(add(3, 5))  # 8
add1 = add(3, 5)
print(add1)  # 8

print(add_no_return(3, 5))  # None

print(add(add(3, 5), 7))


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_many(1, 5, 9, 5))
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print('=' * 50)
#############################################


def operation(choice, *args):
    result = 0
    if choice == "add":
        for i in args:
            result += i
    elif choice == "minus":
        for i in args:
            result -= i
    elif choice == "multiple":
        result = 1
        for i in args:
            result *= i
    elif choice == "divide":
        result = 1
        for i in args:
            result /= i
    else:
        result = "덧셈, 뺄셈, 곱셈, 나눗셈만 할 수 있습니다."
    return result


print(operation("add", 1, 2, 3, 4, 5))
print(operation("minus", 1, 2, 3))
print(operation("multiple", 1, 2))
print(operation("divide", 1, 2, 3, 4))
print(operation("root", 1, 2, 3, 4, 5))
print('=' * 50)


def operation2(choice, lst):
    result = 0
    if choice == "add":
        for i in lst:
            result += i
    elif choice == "minus":
        for i in lst:
            result -= i
    elif choice == "multiple":
        result = 1
        for i in lst:
            result *= i
    elif choice == "divide":
        result = 1
        for i in lst:
            result /= i
    else:
        result = "덧셈, 뺄셈, 곱셈, 나눗셈만 할 수 있습니다."
    return result


print(operation2("add", [1, 2, 3, 4, 5]))
print(operation2("minus", [1, 2, 3]))
print(operation2("multiple", [1, 2]))
print(operation2("divide", [1, 2, 3, 4]))
print(operation2("root", [1, 2, 3, 4, 5]))
print('=' * 50)


#############################################


# 키워드 매개변수: 파라미터 앞에 **를 붙인다. 이러면 딕셔너리 타입으로 전달이 된다.
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name = 'Yoon', country = 'Korea')


def print_kwargs_name(**kwargs):
    if kwargs.__contains__('name'):
        print(kwargs.get('name'))


print_kwargs_name(name ='Yoon', country ='Korea')


#############################################


# 함수의 리턴값은 1개. 그러므로 a + b와 a * b 가 하나로 된 '튜플'을 출력한다
def add_and_mul(a, b):
    return a + b, a * b


print(add_and_mul(3, 4)) #(7, 12)
print(add_and_mul(3, 4)[0]) #7 만 출력
print(add_and_mul(3, 4)[1]) #12 만 출력

#값을 각각 하나씩 리턴받을 수도 있다.
a, b = add_and_mul(3, 4)
print(a) #7
print(b) #12

##############################################


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself('Yoon', 33)
say_myself('Yoon', 33, False)


def say_myself(name, old=13, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself('Yoon')
say_myself('Yoon', 20, False)


######################################################
# 변수의 유효한 범위는 Java와 동일하게 함수 내부에서만이다.

a = 1
id_a1 = id(a)
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a) #2
id_a2 = id(a)
print(id_a1 is id_a2) #False


# Java의 static 처럼 global 명령어를 사용하면 함수 밖 변수도 사용이 가능하다.

a = 1
def vartest2():
    global a
    a += 1

vartest2()
print(a) #2


###########################################################

# python의 lambda는 명령어이며,매개변수를 이용한 표현식의 값을 리턴한다.
add = lambda a, b: a + b

print(add(4, 6))

