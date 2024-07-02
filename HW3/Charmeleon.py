
from Fire import Fire
from math import floor
from Charizard import Charizard


class Charmeleon(Fire):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):
     
        if not isinstance(level, int):
            raise TypeError("level type wrong")
        if 16 <= level <= 31:
            self.level = level
        else: 
            raise ValueError("Level must be 16 < level < 31")
        
        if not isinstance(hit_points, int):
            raise TypeError("hit_points type wrong")
        if 58 < hit_points < 77:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 38 < hit_points < 58")
        
        if not isinstance(attack_power, int):
            raise TypeError("hit_points type wrong")
        if 64 < attack_power < 83:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 51 < attack_power <64")
        
        if not isinstance(defense_power, int):
            raise TypeError("hit_points type wrong")
        if 58 < defense_power < 77:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 42< defense_power < 58")
        
        super().__init__(name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points

     
    def get_damage(self, other):
        return self.get_basic_damage(other) + 2
        
    
    def level_up(self, level_gain):
        if 1 < level_gain < 16:
            self.level = self.level + level_gain
            if self.level > 31:
                return self.evolve()
                
    
    def evolve(self):
        if self.hit_points + 20 > 99:
            self.hit_points = 78
        elif self.hit_points + 20 < 78:
                self.hit_points = 59
        return Charizard(self.name, self.catch_rate, "fire", self.level, self.hit_points +20 , self.attack_power +20 , self.defense_power + 20)

  
    
    def get_type(self):
        return "Charmeleon"

