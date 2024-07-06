
from Fire import Fire
from math import floor
from Charmeleon import Charmeleon
import copy


class Charmander(Fire):
    def __init__(self, name, catch_rate, pokemon_type, __level, __hit_points, __attack_power,__defense_power):
      
        if not isinstance(__level, int):
            raise TypeError("__level type wrong")
        if 1 <= __level <= 15:
            self.__level = __level
        else: 
            raise ValueError("__level must be 1-15")
        
        if not isinstance(__hit_points, int):
            raise TypeError("__hit_points type wrong")
        if 39 <= __hit_points <= 57:
            self.__hit_points = __hit_points
        else:
             ValueError("__hit_points must be 38 < __hit_points < 58")
        
        if not isinstance(__attack_power, int):
            raise TypeError("__hit_points type wrong")
        if 52 <= __attack_power <= 63:
            self.__attack_power = __attack_power
        else:
            ValueError("__attack_power must be 51 < __attack_power <64")
        
        if not isinstance(__defense_power, int):
            raise TypeError("__hit_points type wrong")
        if 43 <= __defense_power <= 57:
            self.__defense_power = __defense_power
        else:
            ValueError("__defense_power must be 42< __defense_power < 58")
        
        super().__init__(name, catch_rate,  pokemon_type)
        self.start_life = self.__hit_points


    def get_type(self):
            return "Charmander"
   
    
    
     
    def get_damage(self, other):
        return self.get_basic_damage(other)

   
    
    
    def level_up(self, level_gain):
        if 0 < level_gain < 17:
            self.__level = self.__level + level_gain
            if self.__level > 15:
                return self.evolve()

    
    def evolve(self):
        if self.__hit_points + 19 > 77:
            self.__hit_points = 57
        elif self.__hit_points + 19 < 58:
            self.__hit_points = 40
        return Charmeleon(self.get_name(), self.get_catch_rate(), "fire", self.get_level(), self.__hit_points +19 , self.__attack_power +12 , self.__defense_power + 15)
         
    def __repr__(self):
        return "The " + self.get_type() + " " +  self.get_name() + " of level " + str(self.__level) + " with " + str(self.__hit_points) + " HP"
    
    
    def absorb(self, damage):
        self.__hit_points = self.__hit_points - damage
   
    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points = int(self.__hit_points - int((self.start_life)*0.1))
            other.absorb(self.get_damage(other))
        
    def can_fight(self):
        if (self.start_life/10)>=self.__hit_points:
            return copy.deepcopy(False)
        else:
            return copy.deepcopy(True)
    
    
    def get_level(self):
        return copy.deepcopy(self.__level)
    
    def get_hit_points(self):
        return copy.deepcopy(self.__hit_points)
    
    def get_defense_power(self):
        return copy.deepcopy(self.__defense_power)
    
    def get_basic_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me(): 
            eff = 2
        else:
            eff = 0.5
        basic_damage = int((((2*self.__level)/5)+2)*(self.__attack_power / other.get_defense_power())*eff)
        return copy.deepcopy(basic_damage)
 