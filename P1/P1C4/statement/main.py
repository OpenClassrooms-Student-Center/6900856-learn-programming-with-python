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
