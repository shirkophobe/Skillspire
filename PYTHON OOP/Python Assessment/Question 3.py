# Question 3: OOP game 

# 1.) Create a base Human class with five attributes: name, strength, intelligence, dexterity, and health.

# 2.) Give a default value of 3 for strength, intelligence, and dexterity. Health should have a default of 100.

# 3.) When an object is constructed from this class it should have the ability to pass a name.

# 4.) Now, add a new method called attack, which when invoked, should attack another Human object that is passed as a parameter. 
# The damage done should be 5 * strength (5 points of damage to the attacked, for each 1 point of strength of the attacker).

# 5.) Create a class for a Ninja, a Wizard, and a Samurai (All of them should inherit from the human class).

# 6.) Wizard should have a default health of 50 and intelligence of 25.

# 7.) Wizard should have a method called heal, which when invoked, heals the Wizard by 10 * intelligence.

# 8.) Wizard should have a method called fireball, which when invoked, decreases the health of whichever object it attacked by some random integer between 20 and 50.

# 9.) Ninja should have a default dexterity of 175.

# 10.) Ninja should have a steal method, which when invoked, attacks an object and increases the Ninjas health by 10.

# 11.) Ninja should have a get_away method, which when invoked, decreases its health by 15.

# 12.) Samurai should have a default health of 200.

# 13.) Samurai should have a method called death_blow, which when invoked should attack an object and decreases its health to 0 if it has less than 50 health.

# 14.) Samurai should have a method called meditate, which when invoked, heals the Samurai back to full health.

import random

class Human:
    def __init__(self, name, strength=3, intelligence=3, dexterity=3, health=100):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.health = health

    def attack(self, other):
        if isinstance(other, Human):
            damage = 5 * self.strength
            other.health -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage. {other.name} now has {other.health} health.")

class Wizard(Human):
    def __init__(self, name):
        super().__init__(name, health=50, intelligence=25)

    def heal(self):
        heal_amount = 10 * self.intelligence
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount}. {self.name} now has {self.health} health.")

    def fireball(self, other):
        if isinstance(other, Human):
            damage = random.randint(20, 50)
            other.health -= damage
            print(f"{self.name} casts fireball on {other.name} for {damage} damage. {other.name} now has {other.health} health.")

class Ninja(Human):
    def __init__(self, name):
        super().__init__(name, dexterity=175)

    def steal(self, other):
        if isinstance(other, Human):
            self.attack(other)
            self.health += 10
            print(f"{self.name} steals and gains 10 health. {self.name} now has {self.health} health.")

    def get_away(self):
        self.health -= 15
        print(f"{self.name} gets away, losing 15 health. {self.name} now has {self.health} health.")

class Samurai(Human):
    def __init__(self, name):
        super().__init__(name, health=200)

    def death_blow(self, other):
        if isinstance(other, Human) and other.health < 50:
            other.health = 0
            print(f"{self.name} delivers a death blow to {other.name}. {other.name} is now at 0 health.")
        else:
            print(f"{self.name} attempted a death blow, but {other.name} has more than 50 health.")

    def meditate(self):
        self.health = 200
        print(f"{self.name} meditates and restores to full health. {self.name} now has {self.health} health.")


wizard = Wizard("Merlin_the_Wizard")
ninja = Ninja("Haybusa_the_Ninja")
samurai = Samurai("Ronin_the_Samurai")
human = Human("Robert_the_Villager")

wizard.fireball(human)
ninja.steal(wizard)
samurai.death_blow(human)
samurai.meditate()
wizard.heal()
ninja.get_away()