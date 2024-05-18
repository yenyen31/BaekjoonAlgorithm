# 리스트 생성
num_list = []
for i in range(9):
    num_list.append(int(input()))  # num_list에 원소 추가하기

print(max(num_list))  # max() 함수 사용해서 최댓값 찾기
print(num_list.index(max(num_list)) + 1)  # index + 1인 값 출력
