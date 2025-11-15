#inheritance

class parent:
  def fun(self):
    print("i am parent")
class child(parent):
  def fun(self):
    print("i am child")
o1=parent()
o2=child()
o1.fun()
o2.fun()
