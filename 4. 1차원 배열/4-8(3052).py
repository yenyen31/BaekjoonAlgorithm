array = []  # 리스트

for i in range(10):  # 리스트 생성
    a = int(input()) % 42  # 입력받은 수를 42로 나눈 나머지를 a에 저장
    if a not in array:  # a가 리스트에 있는지 확인
        array.append(a)  # 새로운 리스트에 추가
print(len(array))  # 리스트 길이 출력
