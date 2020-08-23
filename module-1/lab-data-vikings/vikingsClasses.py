
# Soldier
import random

class Soldier:
    def __init__ (self,health, strength):
        self.health = health
        self.strength = strength

    def attack (self):
        return self.strength   

    def receiveDamage (self, damage):
        self.health -= damage
 
#Viking

class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name 
        self.health = health
        self.strength = strength 

    def attack (self): # En este caso estaría sobreescribiendo?
        return self.strength

    def receiveDamage (self, damage):
        self.health -= damage 
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
         return "Odin Owns You All!" #tristeza que no deja pornerlo en Vikingo :(

# Saxon

class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

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

    def addViking (self, vikingwarrior):
        vi = vikingwarrior 
        if isinstance(vi, vikingwarrior):
            self.vikingArmy.append(vi)

    def addSaxon (self, saxonwarrior):
        sa = saxonwarrior
        if isinstance(sa, saxonwarrior): 
            self.saxonArmy.append(sa)

    def vikingAttack (self):
        ramdonV:random.randint(0,1)
        randomS: ramdon.randint(0,1)
        if Saxon.receiveDamage == Viking.strength: #como llamar a los otros? con super(), el super no seria para la funcion mas cercana?
            saxonArmy -= 1
            return

    def saxonAttack (self):
        if Viking.receiveDamage == Saxon.strength:
            vikingArmy -= 1
            return 

    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
#No pase la 4ta prueba y me salen todos los errores en la linea 68. No di con el error