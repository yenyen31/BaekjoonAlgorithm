hour, min = map(int, input().split())  # 현재 시간 입력 받기
cookingtime = int(input())  # 요리 시간 입력 받기 (분 단위로 입력된다는 점 주의!!)

hour += cookingtime // 60  # 요리 시간을 60분으로 나눈 몫을 현재 "시"에 더해줌
min += cookingtime % 60  # 요리 시간을 60으로 나눈 나머지를 현재 "분"에 더해줌

if min >= 60:  # 현재 시각 "분"이 60 이상인 경우
    hour += 1  # 60분 이상이면 시간에 +1
    # 최종시간으로 현재시간/24한 나머지 값을 출력, 분은 -60한 값을 출력
    print(hour % 24, min - 60)
else:  # 현재 시각 "분"이 60 미만인 경우
    print(
        hour % 24, min
    )  # 최종시간으로 현재시간/24한 나머지 값을 출력, 분은 그대로 출력
