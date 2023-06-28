print('-' * 50)

print("구구단 출력해보기")

ran = range(1, 10)
for i in ran:
    for j in ran:
        print("%d * %d = %2d \t" % (j, i, i * j), end=' ')
    print()