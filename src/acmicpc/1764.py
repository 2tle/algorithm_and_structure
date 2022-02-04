import sys
input = sys.stdin.readline

N, M = map(int, input().split())
NL = []
ML = []
for _ in range(N):
    NL.append(input().replace('\n',''))
for _ in range(M):
    ML.append(input().replace('\n',''))

result = sorted(list( set(NL) & set(ML) ))
print(len(result))
for x in result:
    print(x)