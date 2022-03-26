class Bird():
    def intro(self):
        print("there is may types of birds ")

    def flying(self):
        print("most of birds can fly but some of cant")

class Sparrow(Bird):
    def flying(self):
        print("sparrow can fly")

class Ostrich(Bird):
    def flying(self):
        print("ostrich cannot fly")

obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.flying()
obj_spr.flying()
obj_ost.flying()





