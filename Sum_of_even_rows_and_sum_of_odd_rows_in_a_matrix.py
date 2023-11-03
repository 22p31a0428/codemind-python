n,m=map(int,input().split())
b=[]
d=0
g=0
for i in range(n):
    l=list(map(int,input().split()))
    b.append(l)
for i in range(len(b)):
    if i%2==0:
        d+=sum(b[i])
    else:
        g+=sum(b[i])
print(d,g)