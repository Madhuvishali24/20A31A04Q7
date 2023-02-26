n=str(input("enter the message :  "))
i=0
while i<len(n):
    l=n[i]
    print(chr(ord(n[i])+2),end=" ")
    i=i+1
