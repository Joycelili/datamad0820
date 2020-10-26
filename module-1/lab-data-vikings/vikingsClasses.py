
# Soldier
import random

class Soldier:
    def __init__ (self,health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength   

    def receiveDamage(self, damage):
        self.health -= damage
 
#Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name
    
    def attack (self): # En este caso estaría sobreescribiendo?
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage 
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
         return "Odin Owns You All!" 

# Saxon

class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)

    def attack (self):
        return self.strength   

    def receiveDamage (self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    def _int_(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking (self, viking):
        self.vikingArmy.append(viking)

    def addSaxon (self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack (self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        combat= self.saxon.receiveDamage(self.vik.strength)
        if self.vik.health <= 0:
            vikingArmy.remove(self.vik)
        return combat

    def saxonAttack (self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        combat= self.vik.receiveDamage(self.sax.strength)
        if self.sax.health <= 0:
            saxonArmy.remove(self.sax)
        return combat

    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
