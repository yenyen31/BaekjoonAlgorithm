N = int(input())  # 리스트 요소의 개수

N_list = list(map(int, input().split()))  # 공백으로 구분된 정수 리스트

v = int(input())  # 찾으려고 하는 정수

# 출력
print(N_list.count(v))
