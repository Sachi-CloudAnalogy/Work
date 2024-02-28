# MRO -- method resolution order
# In multiple inheritance it tells the order in which attributes or methods will be accessed in parent classes.

class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")        

class C(A, B):
    pass     

obj = C()
obj.show()

#mro
print(C.__mro__)
print(C.mro())