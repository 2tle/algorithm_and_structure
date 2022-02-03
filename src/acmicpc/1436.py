import sys
input = sys.stdin.readline

N = int(input())
c = 0
for x in range(666,6669999):
    X = str(x)
    if '666' in X:
        c = c + 1
    if N == c:
        print(x)
        break