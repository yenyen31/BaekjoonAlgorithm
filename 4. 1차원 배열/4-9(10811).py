n, m = map(int, input().split())  # n:바구니 개수, m:역순으로 바꾸는 실행 횟수

basket = [i for i in range(1, N + 1)]  # 범위 조심

temp = 0  # 초기화

# 역순으로 바꾸는 실행 반복
# 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만듦
for x in range(m):
    i, j = map(int, input().split())  # i,j 입력 받기
    temp = basket[i - 1 : j]  # i-1번째부터 시작 ~ j까지 슬라이싱
    temp.reverse()  # reverse()로 역순으로 만들기
    basket[i - 1 : j] = temp  # basket의 i-1 ~ j를 temp 변수로 업데이트

# 최종 결과 출력
for x in range(n):
    print(basket[x], end=" ")  # 공백으로 구분해 basket 출력
