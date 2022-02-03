import sys
input = sys.stdin.readline
N,M = map(int, input().split(' '))
suyeol = []
def recursive():
    if len(suyeol) == M:
        print(' '.join(map(str,suyeol)))
        return
    for x in range(1,N+1):
        if x not in suyeol:
            suyeol.append(x)
            recursive()
            suyeol.pop()
recursive()






