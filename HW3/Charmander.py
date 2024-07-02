
from Fire import Fire
from math import floor
from Charmeleon import Charmeleon


class Charmander(Fire):
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
        
        super().__init__(name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points


    def get_type(self):
            return "Charmander"
   
    
    
     
    def get_damage(self, other):
        return self.get_basic_damage(other)

   
    
    
    def level_up(self, level_gain):
        if 0 < level_gain < 17:
            self.level = self.level + level_gain
            if self.level > 15:
                return self.evolve()

    
    def evolve(self):
        if self.hit_points + 19 > 77:
            self.hit_points = 57
        elif self.hit_points + 19 < 58:
            self.hit_points = 40
        return Charmeleon(self.name, self.catch_rate, "fire", self.level, self.hit_points +19 , self.attack_power +12 , self.defense_power + 15)
         
    
 