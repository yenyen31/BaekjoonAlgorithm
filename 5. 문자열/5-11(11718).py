while True:
    try:
        print(input())  # 입력 그대로 출력
    except EOFError:  # 종료 지점
        break
