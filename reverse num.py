n=int(input("enter value="))
rn=0
while(n!=0):
    d=n%10
    rn=rn*10+d
    n//=10
print(rn)
