H, M = map(int, input().split())

if M < 45:  # M이 45보다 작은 경우
    if H == 0:  # 특수 경우: 0시인 경우
        H = 23  # 45분 전이니까 23시로 표기
        print(H, M + 15)  # M는 0~59 의 범위를 갖기 때문에 15를 더하는 것과 같음
    else:  # 0시가 아닌 경우
        print(H - 1, M + 15)
else:  # M이 45보다 큰 경우
    print(H, M - 45)
