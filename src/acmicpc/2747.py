import sys
input = sys.stdin.readline

N = int(input())

bbf = 0
bf = 1
cur = 1
for x in range(3,N+1):
    bbf = bf
    t = bf
    bf = cur
    cur = cur + t
print(cur)