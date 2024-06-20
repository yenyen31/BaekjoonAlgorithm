# 크로아티아 알파벳
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# 입력받기
word = input()

# 규칙 정의하기
for i in croatia:
    word = word.replace(i, "*")  # input 변수와 동일한 이름의 변수에 변환

# 출력
print(len(word))
