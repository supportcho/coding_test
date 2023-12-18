num=int(input())
time=[]
for i in range(num):
    a=tuple(map(int,input().split()))
    time.append(a)
time.sort(key=lambda x:(x[1],x[0]))
current=0
assign=0
for i in time:
    if i[0]>=current:
        assign+=1
        current=i[1]
print(assign)
