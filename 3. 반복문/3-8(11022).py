T = int(input())  # 테스트 케이스 개수

for i in range(1, T + 1):  # Case #1부터 시작해야 하기 때문에 0 ~ T+1로 범위 설정
    a, b = map(int, input().split())
    # 출력형식: "Case #x: A + B = C"
    print(f"Case #{i}: {a} + {b} = {a + b}")
