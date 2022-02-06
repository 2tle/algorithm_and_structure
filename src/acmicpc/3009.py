import sys
input = sys.stdin.readline

X =[]
Y= []
for _ in range(3):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)
px = 0
py = 0
if X[0] == X[1]:
    px = X[2]
elif X[0] == X[2]:
    px = X[1]
else:
    px = X[0]
if Y[0] == Y[1]:
    py = Y[2]
elif Y[0] == Y[2]:
    py = Y[1]
else:
    py = Y[0]
print(px,py)