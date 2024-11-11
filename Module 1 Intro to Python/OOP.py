class Apple:
  def __init__(self):
    self.color = "red"
    self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)

class Apple_Two:
  def __init__(self) -> None:
    self.color = "Blue"
    self.flavor = "Bland"

apple_found_on_the_road = Apple_Two()
print(apple_found_on_the_road.color)

class Apple_Two:
  def __init__(self, color, flavor) -> None: #these are constructors that override default values for a class, instead of just calling values we can use the
    #__str__ to always return a string
    self.color = color
    self.flavor = flavor

  def __str__(self) -> str:
    return "an Apple which is {} and {}".format(self.color, self.flavor)

another_apple = Apple_Two("Bright pink and orange", "Something")


class Piglet: #defining our own methods
  name = "piglet"
  def speak(self):
    print("Oink! I'm {}! Oink!".format(self.name))

