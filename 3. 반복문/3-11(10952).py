while 1:  # 반복문 무한 반복
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    else:
        print(a + b)
