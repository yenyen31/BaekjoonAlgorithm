n = int(input())  # 과목 개수
cur_grade = list(map(int, input().split()))  # 현재 성적 입력 받기

max_grade = max(cur_grade)  # 성적 최댓값
sum_grade = 0

# 최댓값 * 100 값 저장하기
for i in range(n):
    sum_grade += cur_grade[i] / max_grade * 100

new_avg = sum_grade / n  # 새로운 평균 계산
print(new_avg)  # 출력
