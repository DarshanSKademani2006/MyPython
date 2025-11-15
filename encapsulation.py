#encapsulation
class A:
  def __init__(self):
    self.pub=10
    self.__pri=100
  def b(self):
    print(self.__pri)
obj=A()
print(obj.pub)
obj.b()
