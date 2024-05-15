T = int(input())  # 테스트 케이스 개수

for i in range(1, T + 1):  # Case #1부터 시작해야 하기 때문에 0 ~ T+1로 범위 설정
    a, b = map(int, input().split())
    print("Case #" + str(i) + ":", a + b)  # i 출력시에 str(i) 사용하는 점 주의!
