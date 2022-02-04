import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ML = []
R = 0
for _ in range(N):
    ML.append(int(input()))
ML.reverse()
for x in ML:
    R += K//x
    K %= x
print(R)