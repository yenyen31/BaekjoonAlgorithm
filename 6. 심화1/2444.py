# N 입력받기
N = int(input())

# 별의 개수가 증가하는 부분
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 별의 개수가 감소하는 부분
for i in range(n - 1, 0, -1):  # 역순으로 출력
    print(" " * (n - i) + "*" * (2 * i - 1))
