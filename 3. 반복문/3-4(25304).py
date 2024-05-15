x = int(input())  # 영수증에 적힌 총 금액
n = int(input())  # 영수증에 적힌 구매한 물건 종류의 수

sum = 0  # 계산해야 하는 총 금액

for i in range(n):  # 물건 종류의 수대로 반복
    a, b = map(int, input().split())  # 주어지는 각 물건의 개수(a), 가격(b)
    sum += a * b

# 출력
if x == sum:
    print("Yes")
else:
    print("No")
