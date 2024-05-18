n, m = map(int, input().split())  # 바구니 개수(n), 공을 넣는 개수(m)
basket = [0] * n  # 바구니 개수만큼 만들고, 0으로 초기화

for _ in range(m):
    # 내부에서 i, j, k 입력 받기
    # i부터 j까지 배열의 값에 k를 대입
    i, j, k = map(int, input().split())
    for index in range(i, j + 1):
        basket[index - 1] = k  # a[i]부터 a[j]까지 k 대입

for i in range(n):
    print(basket[i], end=" ")
