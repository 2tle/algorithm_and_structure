import sys
input = sys.stdin.readline

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7


for x in range(5,12):
    dp[x] = dp[x-1] + dp[x-2] + dp[x-3]

loop = int(input())
for x in range(loop):
    n = int(input())
    print(dp[n])