import sys  # 빠른 입력받기

T = int(input())  # 테스트 케이스 개수

for i in range(T):  # 0 ~ T-1 까지 반복
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
