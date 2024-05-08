n1, n2, n3 = map(int, input().split())

if n1 == n2 == n3:  # 같은 값 3개
    print(10000 + n1 * 1000)
# 같은 값 2개. 다른 값 1개
elif n1 == n2:
    print(1000 + n1 * 100)
elif n1 == n3:
    print(1000 + n1 * 100)
elif n2 == n3:
    print(1000 + n2 * 100)
else:  # 서로 다른 값
    print(100 * max(n1, n2, n3))  # 최댓값 구하는 max() 사용
