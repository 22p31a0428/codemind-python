p,c,b,m,com=map(int,input().split())
per=(p+c+b+m+com)//5
if(per>=90):
    print("Grade A")
elif(per>=80):
    print("Grade B")
elif(per>=70):
    print("Grade C")
elif(per>=60):
    print("Grade D")
elif(per>=40):
    print("Grade E")
elif(per<40):
    print("Grade F")