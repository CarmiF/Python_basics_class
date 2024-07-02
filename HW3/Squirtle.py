
from Water import Water
from math import floor
from Wartortle import Wartortle

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
        if 44 <= hit_points <= 58:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 44 <= hit_points <= 58")
        
        if not isinstance(attack_power, int):
            raise TypeError("hit_points type wrong")
        if 48 <= attack_power <= 62:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 48 <= attack_power <= 62")
        
        if not isinstance(defense_power, int):
            raise TypeError("hit_points type wrong")
        if 65 <= defense_power <= 79:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 65 <= defense_power <= 79")
        
        super().__init__(name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points
     
    
     
    def get_damage(self, other):
        return self.get_basic_damage(other)
    
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
   