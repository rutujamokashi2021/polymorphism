class A:
    def display(self):
        print('class A')

class B:
    def display(self):
        print('class B')

a = A()
b = B()
for var in (a, b):
    var.display()


