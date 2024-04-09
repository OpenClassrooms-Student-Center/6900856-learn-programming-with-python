class Toolbox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def remove_tool(tool):
        self.tools.remove(tool)

class Screwdriver:
    def __init__(self, size):
        self.size = size

    def tighten(self, screw):
        screw.tighten()

    def loosen(self, screw):
        screw.loosen()

class Hammer:
    def __init__(self, color):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self, nail):
        nail.nail_in()

    def remove(self, nail):
        nail.remove()

class Screw:
   MAX_TIGHTNESS = 5

   def __init__(self):
      self.tightness = 0

   def loosen(self):
      if (self.tightness > 0):
         self.tightness -= 1

   def tighten(self):
      if (self.tightness < self.MAX_TIGHTNESS):
         self.tightness += 1

   def __str__(self):
      return "Screw with tightness {}".format(self.tightness)



class Nail:
   def __init__(self):
      self.in_wall = False

   def nail_in(self):
      if (not self.in_wall):
         self.in_wall = True

   def remove(self):
      if (self.in_wall):
         self.in_wall = False

   def __str__(self):
      return "Nail {}in wall.".format("" if self.in_wall else "not ")

if __name__ == '__main__':
    # Instantiate toolbox
    toolbox = Toolbox()
    # Instantiate Screwdriver with size 10
    screwdriver = Screwdriver(10)
    # Instantiate Hammer with color Red
    hammer = Hammer("Red")
    # Add the both tool on the toolbox with the method add_tool().
    toolbox.add_tool(screwdriver)
    toolbox.add_tool(hammer)

    # Instantiate Screw and Loosen and tighten screw
    screw = Screw()
    screwdriver.tighten(screw)
    print(screw)
    screwdriver.loosen(screw)
    print(screw)

    # Instantiate Nail and hammer in and remove nail
    nail = Nail()
    hammer.hammer_in(nail)
    print(nail)
    hammer.remove(nail)
    print(nail)