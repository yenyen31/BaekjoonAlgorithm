while 1:
    try:  # a, b에 int형이 제대로 입력된 경우 연산 수행
        a, b = map(int, input().split())
        print(a + b)
    except:
        break  # 종료하는 지점 만들어야 함

# try, except 구분 안 해놓을시에 런타임 에러 발생
