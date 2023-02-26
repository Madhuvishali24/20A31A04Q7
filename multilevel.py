class grandfather:
    def A(self):
        print("grandfather")
class father:
    def A(self):
        print("father")
class son(father,grandfather):
    pass
obj1=son()
print(ob1.A())
