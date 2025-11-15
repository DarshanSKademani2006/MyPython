#multiple inheritance 
class A:
  def fun1(self):
    print("day 1")
class B:
  def fun2(self):
    print("day 2")
class C(A,B):
  pass
o1=A()
o1.fun1()
o2=B()
o2.fun2()
