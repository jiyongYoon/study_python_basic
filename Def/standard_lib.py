import datetime

day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 1, 3)

diff = day2 - day1
print(diff)  # 385 days, 0:00:00
print(diff.days)  # 385

print(day1.weekday())  # 1 -> 화요일
print(day1.isoweekday())  # 2 -> 화요일

import time

print(time.time())  # 1690791606.4636033, UTC를 사용하여 현재 시간을 실수 형태로 리턴
print(
    time.localtime())  # time.struct_time(tm_year=2023, tm_mon=7, tm_mday=31, tm_hour=17, tm_min=20, tm_sec=37, tm_wday=0, tm_yday=212, tm_isdst=0)
print(time.asctime())  # Mon Jul 31 17:20:58 2023
print(time.ctime())  # Mon Jul 31 17:23:31 2023

print(time.strftime('%c', time.localtime(time.time())))  # Mon Jul 31 17:23:31 2023
print(time.strftime('%x', time.localtime(time.time())))  # 07/31/23

# for i in range(10):
#     print(i)
#     time.sleep(1)

###################################

import math

print(math.gcd(50, 15))  # 파이썬 3.9 미만은 2개까지만 허용
# print(math.lcm(15, 25))

import random

print(random.randint(1, 10))


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == "__main__":
    print('발표 순서!')
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


def random_sample(data, cnt=None):
    if cnt == None:
        cnt = len(data)
    return random.sample(data, cnt)


if __name__ == "__main__":
    print("발표 순서2!")
    data = [1, 2, 3, 4, 5]
    print(random_sample(data, 2))

    print("발표할 사람 1명")
    print(random.choice(data))
