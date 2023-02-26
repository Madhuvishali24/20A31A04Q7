a=str(input("username:"))


account={"username":"madhu","password":"abc123"}
if (a==account["username"]):
    b=str(input("password:"))
    if(b==account["password"]):
        print("welcome")
    else:
        print("invalid password")
else:
    print("username not found")
