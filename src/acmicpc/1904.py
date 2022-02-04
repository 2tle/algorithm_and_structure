import sys
input = sys.stdin.readline

# N=1 -> 1
# N=2 -> 00,11
# N=3 -> 001 100 111
# N=4 -> 0000 0011 1100 1001 1111
dp = [0,1,2,3,5]

N = int(input())

for x in range(5,N+1):
    dp.append((dp[x-1] + dp[x-2])%15746)
print(dp[N])