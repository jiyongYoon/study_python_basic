a = 10

stomach = 0

도최몇 = int(input("도토리 최대 몇개 먹을수 있음? : "))

print("남은 도토리: " + str(a) + "개")
while a > 0:
    print("도토리 1개 먹음")
    a = a - 1
    stomach = stomach + 1
    print("- 남은 도토리: " + str(a) + "개")
    print("- 남은 배: " + str(도최몇 - stomach) + "개")
    if 도최몇 - stomach == 0: break



