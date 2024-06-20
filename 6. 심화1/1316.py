N = int(input())  # 단어 개수 입력받기
group_word = N  # 그룹 단어 저장할 변수

for i in range(N):
    word = input()  # 단어 입력 받기
    # 알파벳 순서대로 비교
    # 인덱스 범위: 0부터 ~ 단어개수-1 까지
    for j in range(len(word) - 1):
        # 알파벳이 연속적이면 통과
        if word[j] == word[j + 1]:
            continue
        # 알파벳이 연속적X, 개수가 2개 이상이면 그룹단어 포함X
        elif word[j] in word[j + 1 :]:
            group_word -= 1
            break
# 출력
print(group_word)
