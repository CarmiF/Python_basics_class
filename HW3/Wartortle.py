
from Water import Water
from math import floor
from Blastoise import Blastoise


class Wartortle(Water):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):
      
        if not isinstance(level, int):
            raise TypeError("level type wrong")
        if 16 <= level <= 31:
            self.level = level
        else: 
            raise ValueError("Level must be 1-15")
        
        if not isinstance(hit_points, int):
            raise TypeError("hit_points type wrong")
        if 59 <= hit_points <= 78:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 38 < hit_points < 58")
        
        if not isinstance(attack_power, int):
            raise TypeError("attack_power type wrong")
        if 63 <= attack_power <= 82:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 51 < attack_power <64")
        
        if not isinstance(defense_power, int):
            raise TypeError("defense_power type wrong")
        if 80 <= defense_power <= 99:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 42< defense_power < 58")
        
        Water.__init__(self, name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points


    
    
     
    def get_damage(self, other):
        return self.get_basic_damage(other) -1

    def level_up(self, level_gain):
        if 1 <= level_gain <= 16:
            self.level = self.level + level_gain
            if self.level > 31:
                return self.evolve()
            else:
                return None

    
    def evolve(self):
        return Blastoise(self.name, self.catch_rate, "water", self.level, self.hit_points +15 , self.attack_power +15 , self.defense_power + 15)
         
    def get_type(self):
        return "Wartortle"
    
   