num = int(input())  # N은 4의 배수

longnum = 0  # long의 개수 나타내는 변수 초기화

longnum = num // 4  # long의 개수 구하기

for i in range(longnum):
    print("long", end=" ")  # 줄 바꿈 없이 출력하기 -> end=" " 설정하기

print("int")  # 출력 마지막에 "int" 출력하기
