class Boxer:
     def __init__(self,name,size,strength,wins,losses):
        self.name = name
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses
        
     def display_stats(self):
        print(f"Boxer: {self.name}")
        print(f"Size: {self.size}")
        print(f"Strength: {self.strength}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        
        
     def total_score(self):
        return self.size + self.strength + (self.wins) - (self.losses)
        
Boxer1 = Boxer("BoxerOne", size=80, strength=85, wins=10, losses=2)
Boxer2 = Boxer("BoxerTwo", size=75, strength=90, wins=8, losses=1)

print("Boxer 1 Stats:")
Boxer1.display_stats()

print("------------------------------------------------------------")

print("Boxer 2 Stats:")
Boxer2.display_stats()

choice = int(input("Who would you like to bet on? Enter 1 for BoxerOne or 2 for BoxerTwo: "))

if choice == 1:
        if Boxer1.total_score() > Boxer2.total_score():
            print("You bet on BoxerOne and won the bet!")
        else:
            print("You bet on BoxerOne and lost the bet.")
elif choice == 2:
        if Boxer2.total_score() > Boxer1.total_score():
            print("You bet on BoxerTwo and won the bet!")
        else:
            print("You bet on BoxerTwo and lost the bet.")
