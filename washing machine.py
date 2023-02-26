n=int(input())
if 0<n<=2000 :
    print("the time is 25 minutes")
elif 2001<=n<=4000 :
    print("the time is 35 minutes")
elif 4001<=n<=7000:
    print("the time is 45 minutes")
elif 7000<n :
    print("overloaded")
else:
    print("invalid input")
