
from Electric import Electric
from math import floor

def type_message():
    return "Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up"

class Pikachu(Electric):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power, friendship):
      
        if not isinstance(level, int):
            raise TypeError("level type wrong")
        if 1 <= level <= 32:
            self.level = level
        else: 
            raise ValueError("Level must be 1-32")
        
        if not isinstance(hit_points, int):
            raise TypeError("hit_points type wrong")
        if 35 <= hit_points <= 99:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 35 <= hit_points <= 99")
        
        if not isinstance(attack_power, int):
            raise TypeError("attack_power type wrong")
        if 55 <= attack_power <= 99:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 55 <= attack_power <= 99")
        
        if not isinstance(defense_power, int):
            raise TypeError("defense_power type wrong")
        if 40 <= defense_power <= 99:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 40 <= defense_power <= 99")


        if not isinstance(friendship, int):
            raise TypeError("hit_points type wrong")
        if 1 <= friendship <= 5:
            self.friendship = friendship
        else:
            ValueError("Defense_power must be 1<= friendship < 5")
        
        Electric.__init__(self, name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points


   
    def get_type(self):
        return "Pikachu"
    
    # def get_level(self):
    #     return self.level
    
    # def get_hit_points(self):
    #     return self.hit_points

    # def get_defense_power(self):
    #     return self.defense_power

    # def can_fight(self):
    #     if floor(self.start_life/10)>self.hit_points:
    #         return False
    #     else:
    #         return True
    
    def get_damage(self, other):
        if self.type_pokemon in other.get_effective_against_me(): 
            eff = 2
        else:
            eff = 0.5
        damage = floor((((2*self.level)/5)+2)*(self.attack_power/other.get_defense_power())*eff) + self.friendship

        return damage

    # def attack(self, other):
    #     if self.can_fight() and other.can_fight():
    #         self.hit_points = self.hit_points - floor((self.start_life)*0.1)
    #         other.absorb(self.get_damage(other))

    # def absorb(self, damage):
    #     self.hit_points = self.hit_points - damage
    
    def level_up(self, level_gain):
        if 0 < level_gain:
            if self.level + level_gain < 50:
                self.level = self.level + level_gain
            else:
                self.level = 50
         
    
   
    # def get_effective_against_me(self):
    #         return self.effective_against_me
    