class A:
    def A_method(self):
        print("Method A")
class B(A):
    def B_method(self):
        print("Method B")
class C(B):
    def C_menthod(self):
        print("Method C")

obj1 = C()

obj1.A_method()
obj1.B_method()
obj1.C_menthod()