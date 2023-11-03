n=input()
b=[]
for i in n:
    if i not in b:
        b.append(i)
r=""
for i in b:
    r=r+i
if r==n:
    print(True)
else:
    print(False)