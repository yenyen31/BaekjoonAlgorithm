# 풀이방법 1
# print문에 %(나머지)를 이용해 바로 출력하는 방법

n1 = int(input())  # 입력받는 첫 번째 숫자
n2 = int(input())  # 입력받는 두 번째 숫자

# (3) 출력
print(n1 * (n2 % 10))

# (4) 출력
print(n1 * ((n2 % 100) // 10))

# (5) 출력
print(n1 * (n2 // 100))

# (6) 출력
print(n1 * n2)  # 답 도출

# 풀이방법 2
# 결과값을 list 변수에 담고, 출력하는 방법
n1 = int(input())
n2 = list(map(int, input()))

result = []

for i in range(len(n2), 0, -1):  # for문 이용
    result.append(n1 * n2[i - 1])

print(result[0], result[1], result[2], sep="\n")
print(result[0] + (result[1] * 10) + result[2] * 100)
