import sys
input = sys.stdin.readline

N = int(input())
DP = [0,1]

for x in range(2,N+1):
    DP.append((DP[x-1]+DP[x-2])%1000000007)
print(DP[N])