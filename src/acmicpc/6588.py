import sys
input = sys.stdin.readline

CON = 1000001
checker = [True for _ in range(CON)]
for i in range(2, 1001):
    if checker[i]:
        for j in range(2*i, CON, i):
            checker[j]=False

while True:
    n = int(input())
    if n ==0:
        break
    i=3
    for i in range(3, len(checker)):
        if checker[i] and checker[n-i]:
            print('{0} = {1} + {2}'.format(n,i,n-i))
            break
    if i == len(checker):
        print("Goldbach's conjecture is wrong.")