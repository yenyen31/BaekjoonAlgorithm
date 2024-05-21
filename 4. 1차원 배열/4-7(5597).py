std = [i for i in range(1, 31)]  # 학생 번호 리스트, 범위 주의

for _ in range(28):  # 제출한 학생
    # 입력받은 숫자를 리스트에서 제거
    data = int(input())
    std.remove(data)

print(min(std))  # 가장 작은 번호
print(max(std))  # 다음으로 큰 번호
