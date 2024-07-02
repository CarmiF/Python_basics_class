
from math import floor
from abc import ABC, abstractmethod
import copy
class Pokemon(ABC):

    def __init__(self, name, catch_rate):
       
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
    
    @abstractmethod
    def get_hit_points(self):
        pass
    
    @abstractmethod
    def get_defense_power(self):
        pass

    
    @abstractmethod
    def can_fight(self):
       pass
    
    @abstractmethod
    def attack(self, other):
       pass

    def get_name(self):
        return copy.deepcopy(self.__name)
    
    def get_catch_rate(self):
        return copy.deepcopy(self.__catch_rate)
    
    def full_print(self):
        print("The " + self.get_name() + self.get_name() + " catch_rate: " + str(self.catch_rate) + " pokemon_type: " + " level: " + str(self.level) + " hit_points: " +  str(self.hit_points) + " attack_power: " + str(self.attack_power) + " defense_power: " + str(self.defense_power))

    
    @abstractmethod
    def absorb(self, damage):
        pass

    @abstractmethod
    def get_effective_against_others(self):
        pass

    @abstractmethod
    def get_effective_against_me(self):
        pass    
   
    
    @abstractmethod
    def get_level(self):
        return self.level
    
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_pokemon_type(self):
        pass   

    @abstractmethod
    def get_damage(self, other):
        pass
    
    @abstractmethod
    def level_up(self, level_gain):
      pass

    @abstractmethod
    def evolve(self, level_gain):
      pass
    
    

class Pokemon_helper(Pokemon):
    def __repr__(self):
        return "The " + self.get_type() + " " +  self.get_name() + " of level " + str(self.level) + " with " + str(self.hit_points) + " HP"
    def get_name(self):
        return self.name
    
    def get_effective_against_me(self):
        return self.effective_against_me
    def get_effective_against_others(self):
        return self.effective_against_others
    def absorb(self, damage):
        self.hit_points = self.hit_points - damage
   
    def attack(self, other):
        a = other.hit_points
        if self.can_fight() and other.can_fight():
            self.hit_points = int(self.hit_points - int((self.start_life)*0.1))
            other.absorb(self.get_damage(other))
        
    def can_fight(self):
        if (self.start_life/10)>=self.hit_points:
            return False
        else:
            return True
    
    
    def get_level(self):
        return copy.deepcopy(self.level)
    
    def get_hit_points(self):
        return copy.deepcopy(self.hit_points)
    
    def get_defense_power(self):
        return copy.deepcopy(self.defense_power)
    
    def get_basic_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me(): 
            eff = 2
        else:
            eff = 0.5
        basic_damage = int((((2*self.level)/5)+2)*(self.attack_power / other.get_defense_power())*eff)
        return copy.deepcopy(basic_damage)
        
