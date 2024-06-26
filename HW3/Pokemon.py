
from math import floor
class Pokemon:

    def __init__(self, name, catch_rate):
        pass
        # if not isinstance(name, str) or isinstance(catch_rate, int):
        #     raise TypeError("Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up")
        
        if not isinstance(name, str):
            raise TypeError("name type wrong")
        else: 
            self.name = name


        if not isinstance(catch_rate, int):
            raise TypeError("catch_rate type wrong")
        if 40 <= catch_rate <= 45:
            self.catch_rate = catch_rate
        else: 
            raise ValueError("catch_rate must be 40 <= catch_rate <= 45")
        

    def get_hit_points(self):
        return self.hit_points

    def get_defense_power(self):
        return self.defense_power

    def can_fight(self):
        if floor(self.start_life/10)>self.hit_points:
            return False
        else:
            return True
    
    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.hit_points = self.hit_points - floor((self.start_life)*0.1)
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.hit_points = self.hit_points - damage
    
    def get_effective_against_me(self):
        return self.effective_against_me
    
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "The " + self.get_type() + " " +  self.get_name() + " of " + str(self.level) + " with " + str(self.hit_points) + " HP."
    
    def full_print(self):
        print(self.get_type() + " " + self.get_name() + " catch_rate: " + str(self.catch_rate) + " pokemon_type: " + " level: " + str(self.level) + " hit_points: " +  str(self.hit_points) + " attack_power: " + str(self.attack_power) + " defense_power: " + str(self.defense_power))



