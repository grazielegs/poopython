class Dog:
    def __init__(self, name, color, size, personality):
        self.name = name
        self.color = color
        self.size = size
        self.personality = personality

    def bark(self):
        print("Woof!")
        
    def bork(self):
        print("Bork!")

shiberino = Dog("Shiberino", "caramel", "pupper", "dumb")
print(shiberino.name)
shiberino.bork()

fido = Dog("Fido", "brown", "smol", "funny")
print(fido.name)
fido.bark()
