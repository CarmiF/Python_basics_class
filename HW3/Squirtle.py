
from Water import Water
from math import floor
from Wartortle import Wartortle

def type_message():
    return "Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up"

class Squirtle(Water):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):
      
        if not isinstance(level, int):
            raise TypeError("level type wrong")
        if 1 <= level <= 15:
            self.level = level
        else: 
            raise ValueError("Level must be 1-15")
        
        if not isinstance(hit_points, int):
            raise TypeError("hit_points type wrong")
        if 39 <= hit_points <= 57:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 38 < hit_points < 58")
        
        if not isinstance(attack_power, int):
            raise TypeError("hit_points type wrong")
        if 52 <= attack_power <= 63:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 51 < attack_power <64")
        
        if not isinstance(defense_power, int):
            raise TypeError("hit_points type wrong")
        if 43 <= defense_power <= 57:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 42< defense_power < 58")
        
        Water.__init__(self, name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points


    def __repr__(self):
        return "The Squirtle " + self.get_name() + " of " + str(self.level) + " with " + str(self.hit_points) + " HP."
    
    def full_print(self):
        print("Squirtle " + self.get_name() + " catch_rate: " + str(self.catch_rate) + " pokemon_type: " + " level: " + str(self.level) + " hit_points: " +  str(self.hit_points) + " attack_power: " + str(self.attack_power) + " defense_power: " + str(self.defense_power))


    def get_hit_points(self):
        return self.hit_points

    def get_defense_power(self):
        return self.defense_power

    def can_fight(self):
        if floor(self.start_life/10)>self.hit_points:
            return False
        else:
            return True
    
    def get_damage(self, other):
        if self.type_pokemon == other.get_effective_against_me(): 
            eff = 2
        else:
            eff = 0.5
        
        damage = floor((((2*self.level)/5)+2)*(self.attack_power/other.defense_power)*eff)
        return damage

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.hit_points = self.hit_points - floor((self.start_life)*0.1)
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.hit_points = self.hit_points - damage
    
    def level_up(self, level_gain):
        if 1 <= level_gain <= 16:
            self.level = self.level + level_gain
            if self.level > 15:
                return self.evolve()
            else:
                return None

    
    def get_type(self):
            return "Squirtle"
    
    def evolve(self):
        return Wartortle(self.name, self.catch_rate, "water", self.level, self.hit_points +15 , self.attack_power +15 , self.defense_power + 15)
         
    def get_effective_against_me(self):
        return self.effective_against_me
    def get_level(self):
        return self.level


