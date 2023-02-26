#0,0,7,6,14,12,21,18,28,24,35,30,42,36,49,42,56
n=int(input())
a=0
b=0
for i in range(1,n+1):
    
    if(n%2==0):
        a=7+a
        
    else :
        b=6+b
        
if(n%2==0):
    print(a)
else:
    print(b)
