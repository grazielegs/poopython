class Doge: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("bark!")

class Smol(Doge):
    def bark(self):
        print("bork")
        
class Dogge(Doge):
    def bark(self):
        print("bork bork!")
        
class Doggo(Doge):
    def bark(self):
        print("bork bork BORK!")

huskerino = Doggo("Louis", "caramel")
huskerino.bark()
