n=int(input("enter the input : "))
s=0
while (n!=0) :
    r=n%10
    s=s+(r*r*r)
    n=n//10
if s==n :
    print("armstrong")
else :
    print("not an armstrong")
