N = int(input())

for i in range(N):
    star = "*" * (i + 1)
    print(star.rjust(N))  # 오른쪽을 기준으로 정렬하는 rjust()이용
