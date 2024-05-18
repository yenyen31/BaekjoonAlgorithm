N, M = map(int, input().split())

basket = list(range(N + 1))  # 바구니 리스트 생성

for _ in range(M):  # M만큼 반복
    i, j = map(int, input().split())  # i, j 입력받기
    basket[i], basket[j] = basket[j], basket[i]  # 교환

print(*arr[1:])  # basket 첫 번째 이후부터 요소 모두 출력
