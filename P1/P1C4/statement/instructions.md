# Instructions

In the last chapter, you wrote classes based on the toolbox example - now it’s time to use them.

```
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
        pass

    def loosen(self, screw):
        pass

class Hammer:
    def __init__(self, color):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self, nail):
        pass

    def remove(self, nail):
        pass
```
Copy these Screw and Nail classes into your project:

```
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
```

**Make doing the following things:**
1. Instantiate a toolbox, a screwdriver, and a hammer.
2. Put the hammer and screwdriver in the toolbox.
3. Instantiate a screw, and tighten it using the screwdriver. Print the screw before and after it's been tightened. (You will need to define both methods of the screwdriver class, it's currently define by `pass`).
4. Instantiate a nail, then hammer it in using the hammer. Print the nail before and after it’s been hammered in. (You will need to define both methods of the screwdriver class, it's currently define by `pass`).

