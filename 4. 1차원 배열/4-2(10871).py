N, X = map(int, input().split())

# 수열 (A) 입력받기
A = list(map(int, input().split()))

# 출력
for i in range(N):
    if A[i] < X:  # X보다 작은 수 출력
        print(A[i], end=" ")
