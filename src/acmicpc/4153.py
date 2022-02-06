import sys
input = sys.stdin.readline

while True:
    L = sorted(list(map(int, input().split())))
    if L[0] == L[1] and L[1] == L[2] and L[0] == 0:
        break
    if L[2] * L[2] == L[0] * L[0] + L[1] * L[1]:
        print("right")
    else:
        print("wrong")
