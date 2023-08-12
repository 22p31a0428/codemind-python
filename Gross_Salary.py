bs=int(input())
if bs<=10000:
    da=bs*0.80
    hra=bs*0.20
elif bs<=20000:
    da=bs*0.90
    hra=bs*0.25
elif bs>20000:
    da=bs*0.95
    hra=bs*0.30
print(f"{bs+da+hra:.2f}")