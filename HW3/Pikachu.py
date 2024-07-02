
from Electric import Electric
from math import floor


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
    
    
     
    
     
    def get_damage(self, other):
        return self.get_basic_damage(other) + self.friendship
    
    def level_up(self, level_gain):
        if 0 < level_gain:
            if self.level + level_gain < 50:
                self.level = self.level + level_gain
            else:
                self.level = 50
         
    def evolve(self, level_gain):
       pass
    