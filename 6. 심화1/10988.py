# 문자 입력받기
word = list(input())

# 문자 비교하기
if word == word[::-1]:
    print(1)
else:
    print(0)
