import sys
input = sys.stdin.readline

def solution(n):
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    for x in range(4,1001):
        dp[x] = dp[x-1] + 2 * dp[x-2]
    print(dp[n] % 10007)

solution(int(input()))