n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    if i%2==0:
        c+=l[i]
print(c)