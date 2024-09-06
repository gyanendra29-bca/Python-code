n=int(input("enter the value="))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n//=10
    if(t==r):
        print("number is pailendrom")
    else:
        print("numbe is not pailendrom")
