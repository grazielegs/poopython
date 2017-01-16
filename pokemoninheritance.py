class Pokemon: 
    def __init__(self, name, tipe): # couldnt use 'type' word :/
        self.name = name
        self.tipe = tipe

class Fire(Pokemon):
    def burn(self):
        print("Pokemon use: BURNNNN")
        
class Water(Pokemon):
    def watergun(self):
        print("Pokemon use: WATER GUNNN")
        
class Leaf(Pokemon):
    def treattack(self):
        print("Pokemon use: TRE ATTACK")

charizard = Fire("Charizard", "Fire")
print(charizard.tipe)
charizard.burn()
