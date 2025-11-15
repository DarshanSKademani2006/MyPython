#polymorphism
class bird:
  def speak(self):
    print("i chirp")
class parrot(bird):
  def speak(self):
    print("i mimic")
o=parrot()
o.speak()
