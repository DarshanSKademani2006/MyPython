class area:
  def __init__(self,r):
    self.r=r
  def circle(self):
    return 3.14*self.r**2
o=area(5)
print(o.circle())
