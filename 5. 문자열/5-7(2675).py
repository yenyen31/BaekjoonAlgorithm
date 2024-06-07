a = int(input())  # 입력받기

#
for i in range(a):
    b, c = input().split()
    for i in range(len(c)):
        print(int(b) * c[i], end="")
    print()
