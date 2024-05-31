# 필요한 피스 수를 리스트로 선언
piece = [1, 1, 2, 2, 2, 8]

# 킹, 퀸, 룩, 비숍, 나이트, 폰을 리스트 형태로 입력받음
num = list(map(int, input().split()))
result = 0  # 계산값 담을 변수 초기화

# 피스 계산하기
for i in range(len(piece)):
    # 요구하는 피스 수 - 가지고 있는 피스 수 = 필요한 피스 수
    result = piece[i] - num[i]
    print(result, end=" ")
