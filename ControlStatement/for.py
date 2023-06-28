test_list = ["one", "two", "three"]
for word in test_list:
    print(word)

a = [(1, 5), (3, 4), (7, -2)]
for pair in a:
    print(pair[0] + pair[1])

for (left, right) in a:
    print(left + right)

print('-' * 50)

point_list = [(1, 100), (2, 40), (3, 56), (4, 70), (5, 90)]
cut_line = float(input("이번 시험의 커트라인을 입력하세요: "))
average = 0
for (num, point) in point_list:
    average = average + point
    if point >= cut_line:
        print(str(num) + "번 통과")
    else:
        message1 = "%d번 %d점 부족하여 실패" % (num, cut_line - point)
        message2 = "{0}번 {1}점 부족하여 실패".format(num, cut_line - point)
        print(message1)
        print(message2)
print("전체 평균은 {0}점 입니다.".format(average / len(point_list)))



print('-' * 50)

b = range(0, 10) # 1 <= x < 10 까지의 range 객체를 만들어줌
for idx in b:
    print(idx)

# java의 for(int i = 0; i < 10; i++) 와 비슷하구만
for idx in range(5, 9):
    print(idx)


