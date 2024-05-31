# 문자열로 입력 받기
a, b = input().split()

# 리스트로 변환
list_a = list(a)
list_b = list(b)

# reverse() 이용해 리스트 안에 원소 뒤집기
list_a.reverse()
list_b.reverse()

# 정수형 변수에 거꾸로된 수 넣기
aa = int(list_a[0] + list_a[1] + list_a[2])
bb = int(list_b[0] + list_b[1] + list_b[2])

# 둘 중에 더 큰 값 찾기
print(max(aa, bb))
