class A:
    var1="base class"
class B(A):
    var2="child class1"
class C(A):
    var3="child class2"
obj1=A()
obj2=B()
obj3=C()
print(obj1.var1)
print(obj2.var2)
print(obj3.var3)

