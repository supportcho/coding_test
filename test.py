from collections import deque
def bfs(v):
    #v는 시작위치
    q=deque([v])
    visited[v]=0
    while q:
        x=q.popleft()
        last=x
        if x==m:
            print(visited[m])
            break
        for i in range(3):
            if i==0:
                x=last+dx[i]
            elif i==1:
                x=last+dx[i]
            else:
                x=last*dx[i]
            if x>=0 and x<=100000 and visited[x]==0:
                visited[x]=visited[last]+1
                q.append(x)


visited=[0]*1000001
dx=[1,-1,2]
n,m=map(int,input().split())
bfs(n)