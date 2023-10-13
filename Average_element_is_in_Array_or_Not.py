n=int(input())
l=list(map(int,input().split()))
avg=(sum(l))//n
x=False
if avg in l:
    x=True
print(x)