
from Fire import Fire
from math import floor
from Charizard import Charizard

def type_message():
    return "Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up"

class Charmeleon(Fire):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):
        # if not isinstance(level, int) or isinstance(hit_points, int) or isinstance(attack_power, int) or isinstance(defense_power, int):
        #     raise TypeError("Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up")

        if not isinstance(level, int):
            raise TypeError("level type wrong")
        if 16 <= level <= 31:
            self.level = level
        else: 
            raise ValueError("Level must be 1-15")
        
        if not isinstance(hit_points, int):
            raise TypeError("hit_points type wrong")
        if 58 <= hit_points <= 77:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 38 < hit_points < 58")
        
        if not isinstance(attack_power, int):
            raise TypeError("hit_points type wrong")
        if 64 <= attack_power <=83:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 51 < attack_power <64")
        
        if not isinstance(defense_power, int):
            raise TypeError("hit_points type wrong")
        if 58<= defense_power <= 77:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 42< defense_power < 58")
        
        Fire.__init__(self, name, catch_rate,  pokemon_type)
        self.life = self.hit_points


    def __repr__(self):
        return "The Charmeleon " + self.get_name() + " of " + str(self.level) + " with " + str(self.hit_points) + " HP."
    
     
    def full_print(self):
        print("Charmeleon " + self.get_name() + " catch_rate: " + str(self.catch_rate) + " pokemon_type: " + " level: " + str(self.level) + " hit_points: " +  str(self.hit_points) + " attack_power: " + str(self.attack_power) + " defense_power: " + str(self.defense_power))


    def get_hit_points(self):
        return self.hit_points

    def get_defense_power(self):
        return self.defense_power

    def can_fight(self):
        if floor(self.hit_points/10)>self.life:
            return False
        else:
            return True
    
    def get_damage(self, other):
        if self.get_effective_against_others == other.get_effective_against_me: 
            eff = 2
            print("2")
        else:
            eff = 0.5
        
        damage = floor((((2*self.level)/5)+2)*(self.attack_power/other.defense_power)*eff + 2)
        return damage

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.life = (self.life)*0.9
            other.absorb(self.get_damage)

    def absorb(self, damage):
        self.life = self.life - damage
    
    def level_up(self, level_gain):
        if 0 <= level_gain <= 16:
            self.level = self.level + level_gain
            if self.level > 31:
                self.evolve()
    
    def evolve(self):
        self = Charizard(self.name, self.catch_rate, "fire", self.level, self.hit_points +20 , self.attack_power +20 , self.defense_power + 20)

    





