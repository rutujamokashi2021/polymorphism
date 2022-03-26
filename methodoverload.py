class OverloadDemo:
  # define no argument method
  def method(self):
    print("No argument")
  # define 1 argument method
  def method(self, a):
    print("One argument")
  # define 2 argument method
  def method(self,a, b):
    print("Two arguments")
# create object of class
obj = OverloadDemo()
# call method with a single argument
obj.method(10)