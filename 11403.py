import sys

a = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]


for k in range(a):
    for b in range(a):
        for c in range(a):
            if arr[b][k] and arr[k][c]:
                arr[b][c]=1

for i in range(a):
    for j in range(a):
        print(arr[i][j], end=" ")
    print()       