n,m=map(int,input().split())
mat=[]
for i in range(n):
    i=list(map(int,input().split()))[:m:]
    mat.append(i)
s=0
for i in mat:
    for every_value in i:
        s+=every_value
print(s)