import sys
input = sys.stdin.readline
T = int(input())


ER = [False, False] + [True]*(10000)
for x in range(2,10000):
    if ER[x]:
        for y in range(2*x,10000,x):
            ER[y] = False

for x in range(T):
    N = int(input())
    left = N//2
    right = N//2
    for y in range(10000):
        if ER[left] and ER[right]:
            print(left, right)
            break
        left -= 1
        right += 1


