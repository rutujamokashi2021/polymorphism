class A():
    def display(self):
        print("hello")

class B():
    def display(self):
        print("how r u???")

obja = A()
objb = B()

for var in (obja , objb):
    var.display()
