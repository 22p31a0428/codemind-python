n=int(input())
l=list(map(int,input().split()))
c=0
f=0
for i in l:
    if i%2==0:
        c+=i
    else:
        f+=i
print(abs(f-c))