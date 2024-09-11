import random

class BigCat:
    def __init__(self, speed=5, strength=5, intelligence=5, health=5, durability=5):
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.health = health
        self.durability = durability

    def is_alive(self):
        return self.health > 0

class Lion(BigCat):
    def __init__(self):
        super().__init__(strength=50, health=50)
    
    def king(self, other):
        if isinstance(other, Cheetah) and random.random() > 0.6:
            print("Cheetah escaped unscathed!")
        else:
            print("Lion roars as the king! Depleting attributes of", type(other).__name__)
            other.speed = 0
            other.strength = 0
            other.intelligence = 0
            other.health = 0
            other.durability = 0

class Leopard(BigCat):
    def __init__(self):
        super().__init__(strength=30, intelligence=30, health=30)
    
    def attack(self, other):
        if isinstance(other, Lion):
            print("Leopard attacking Lion!")
            other.king(self)
        elif isinstance(other, Cheetah) and random.random() > 0.6:
            print("Cheetah escaped the Leopard's attack unscathed!")
        else:
            print("Leopard attacks", type(other).__name__)
            other.health -= 15

class Cheetah(BigCat):
    def __init__(self):
        super().__init__(speed=75, strength=25, intelligence=25, health=25, durability=25)
    
    def run(self, other):
        if isinstance(other, Leopard):
            print("Cheetah runs away from Leopard!")
            other.attack(self)
        elif isinstance(other, Lion):
            print("Cheetah runs away from Lion!")
            other.king(self)
        else:
            print("Cheetah is safe for now.")
        
        if other.is_alive():
            print("Cheetah loses 20 health points from running away.")
            self.health -= 20

lion = Lion()
leopard = Leopard()
cheetah = Cheetah()

animals = [lion, leopard, cheetah]

turn = 0
while any(animal.is_alive() for animal in animals):
    turn += 1
    print(f"\n--- Turn {turn} ---")
    
    if lion.is_alive():
        target = random.choice([animal for animal in animals if animal is not lion and animal.is_alive()])
        print("Lion's turn:")
        lion.king(target)
    
    if leopard.is_alive():
        target = random.choice([animal for animal in animals if animal is not leopard and animal.is_alive()])
        print("Leopard's turn:")
        leopard.attack(target)
    
    if cheetah.is_alive():
        target = random.choice([animal for animal in animals if animal is not cheetah and animal.is_alive()])
        print("Cheetah's turn:")
        cheetah.run(target)
    
    alive_animals = [animal for animal in animals if animal.is_alive()]
    if len(alive_animals) == 1:
        winner = alive_animals[0]
        print(f"\n{type(winner).__name__} is the winner!")
        break
    elif len(alive_animals) == 0:
        print("\nNo animals left alive! Draw.")
        break

