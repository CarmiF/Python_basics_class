
from Water import Water
from math import floor


class Blastoise(Water):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):
      
        if not isinstance(level, int):
            raise TypeError("level type wrong")
        if 31 < level <50:
            self.level = level
        else: 
            raise ValueError("Level must be 1-15")
        
        if not isinstance(hit_points, int):
            raise TypeError("hit_points type wrong")
        if 80 <= hit_points <= 99:
            self.hit_points = hit_points
        else:
             ValueError("hit_points must be 38 < hit_points < 58")
        
        if not isinstance(attack_power, int):
            raise TypeError("hit_points type wrong")
        if 83 <= attack_power <= 99:
            self.attack_power = attack_power
        else:
            ValueError("attack_power must be 51 < attack_power <64")
        
        if not isinstance(defense_power, int):
            raise TypeError("hit_points type wrong")
        if 100 <= defense_power <= 115:
            self.defense_power = defense_power
        else:
            ValueError("Defense_power must be 42< defense_power < 58")
        
        super().__init__(name, catch_rate,  pokemon_type)
        self.start_life = self.hit_points

    
    def get_damage(self, other):
        return self.get_basic_damage(other) -2

    def level_up(self, level_gain):
        if 0 < level_gain:
            if self.level + level_gain < 50:
                self.level = self.level + level_gain
            else:
                self.level = 50
                
    def get_type(self):
        return "Blastoise"
    
    def evolve(self, level_gain):
      pass

