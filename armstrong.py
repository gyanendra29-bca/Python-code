n=input("enter the number=")
s=0
l=len(n)
for i in n:
    
    d=int(i)
    s+=d**l
if(int(n)==s):
    print(" number is armstrong")
else:
    print("not armstrong")
