

from math import floor
from abc import ABC, abstractmethod
import copy
class Pokemon(ABC):
    @abstractmethod
    def __init__(self, name, __catch_rate):
       
        if not isinstance(name, str):
            raise TypeError("name type wrong")
        else: 
            self.__name = name


        if not isinstance(__catch_rate, int):
            raise TypeError("__catch_rate type wrong")
        if 40 <= __catch_rate <= 45:
            self.__catch_rate = __catch_rate
        else: 
            raise ValueError("__catch_rate must be 40 <= __catch_rate <= 45")
    
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
        print("The " + self.get_name() + self.get_name() + " __catch_rate: " + str(self.__catch_rate) + " pokemon_type: " + " level: " + str(self.level) + " hit_points: " +  str(self.hit_points) + " attack_power: " + str(self.attack_power) + " defense_power: " + str(self.defense_power))

    
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
    
    

# class Pokemon_helper(Pokemon):
    # def __repr__(self):
    #     return "The " + self.get_type() + " " +  self.get_name() + " of level " + str(self.level) + " with " + str(self.hit_points) + " HP"
    # def get_name(self):
    #     return copy.deepcopy(self.name)
    
    # def absorb(self, damage):
    #     self.hit_points = self.hit_points - damage
   
    # def attack(self, other):
    #     a = other.hit_points
    #     if self.can_fight() and other.can_fight():
    #         self.hit_points = int(self.hit_points - int((self.start_life)*0.1))
    #         other.absorb(self.get_damage(other))
        
    # def can_fight(self):
    #     if (self.start_life/10)>=self.hit_points:
    #         return copy.deepcopy(False)
    #     else:
    #         return copy.deepcopy(True)
    
    
    # def get_level(self):
    #     return copy.deepcopy(self.level)
    
    # def get_hit_points(self):
    #     return copy.deepcopy(self.hit_points)
    
    # def get_defense_power(self):
    #     return copy.deepcopy(self.defense_power)
    
    # def get_basic_damage(self, other):
    #     if self.get_pokemon_type() in other.get_effective_against_me(): 
    #         eff = 2
    #     else:
    #         eff = 0.5
    #     basic_damage = int((((2*self.level)/5)+2)*(self.attack_power / other.get_defense_power())*eff)
    #     return copy.deepcopy(basic_damage)
        


class conditions:
    def __init__(self, conditions_list, name):
        if isinstance(conditions_list, list):
            self.__upper_bound = conditions_list[1]
            self.__bottom_bound = conditions_list[0]
            self.__name = name
        else:
            raise TabError("conditions_list not list")
    
    
    def check_condition(self, num):
        if not isinstance(num, int):
            raise TypeError(f"{self.__name} type wrong")
        if self.__bottom_bound <= num <= self.__upper_bound:
            return True
        else:
            raise ValueError(f"{self.__name} is not {self.__bottom_bound} < {self.__name} < {self.__upper_bound}")



