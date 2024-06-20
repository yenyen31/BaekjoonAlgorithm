word = input().upper()  # 문자열 입력을 대문자로 변환
word_list = list(
    set(word)
)  # word 문자열에서 중복된 문자를 제거한 후, 이를 리스트로 변환하여 word_list 변수에 저장

cnt = []  # 문자를 저장할 리스트 생성
for i in word_list:  # word_list의 각 문자에 대해 반복
    count = word.count  # word 문자열의 count 메서드를 count 변수에 저장
    cnt.append(
        count(i)
    )  # 현재 문자 i가 word 문자열에 몇 번 등장하는지 세고, 그 결과를 cnt 리스트에 추가

# cnt 리스트에서 가장 큰 값(max(cnt))이 여러 번 등장하는지 확인. (가장 많이 등장한 문자가 여러 개인지 확인)
if cnt.count(max(cnt)) > 1:
    print("?")  # 가장 많이 등장한 문자가 여러 개라면 ?를 출력

else:  # cnt 리스트에서 가장 큰 값(max(cnt))의 인덱스를 찾고, 해당 인덱스에 있는 word_list의 문자를 출력
    print(word_list[(cnt.index(max(cnt)))])
