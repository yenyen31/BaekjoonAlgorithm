N = int(input())  # 실행 횟수 입력 받기
# A, B = map(int, input().split())

for i in range(1, N + 1):
    A, B = map(int, input().split())  # 두 수 A, B 입력받기
    print(A + B)
