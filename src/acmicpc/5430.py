import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


for x in range(T):
    status = False
    Rstauts = False
    p = input().replace('\n','').replace('RR','')
    n = int(input())
    deq = deque(input().replace('[','').replace(']','').replace('\n','').split(','))
    if n == 0:
        deq = deque()
    for k in p:
        if k == 'R':
            if Rstauts == True:
                Rstauts = False
            else:
                Rstauts = True
        else:
            if deq:
                if Rstauts:
                    deq.pop()
                else:
                    deq.popleft()
            else:
                status = True
                print('error')
                break
    if status == False:
        if Rstauts:
            deq.reverse()
        print('[' + ",".join(deq) + ']')
