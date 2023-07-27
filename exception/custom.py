class MyError(Exception):
    pass



def say_nick(nick):
    if nick == '바보':
        raise MyError(nick)
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(f"허용되지 않는 별명입니다. 시도한 별명={e}")