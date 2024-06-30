
from math import floor
from abc import ABC, abstractmethod

class Pokemon(ABC):

    def __init__(self, name, catch_rate):
        # if not isinstance(name, str) or isinstance(catch_rate, int):
        #     raise TypeError("Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up")
        
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
        return self.hit_points
    
    @abstractmethod
    def get_defense_power(self):
        return self.defense_power

    
    @abstractmethod
    def can_fight(self):
        if floor(self.start_life/10)>self.hit_points:
            return False
        else:
            return True
    
    @abstractmethod
    def attack(self, other):
        a = other.hit_points
        if self.can_fight() and other.can_fight():
            self.hit_points = self.hit_points - floor((self.start_life)*0.1)
            other.absorb(self.get_damage(other))
        print("attack pok "+ self.get_pokemon_type() + " " + str(self.hit_points))
        print("defend pok " + other.get_pokemon_type() + " " + str(other.hit_points) + " damage " + str(a- other.hit_points))

    def get_name(self):
        return self.name
    def get_catch_rate(self):
        return self.catch_rate
    
    def full_print(self):
        print("The " + self.get_name() + self.get_name() + " catch_rate: " + str(self.catch_rate) + " pokemon_type: " + " level: " + str(self.level) + " hit_points: " +  str(self.hit_points) + " attack_power: " + str(self.attack_power) + " defense_power: " + str(self.defense_power))

    
    @abstractmethod
    def absorb(self, damage):
        self.hit_points = self.hit_points - damage
    
    @abstractmethod
    def get_effective_against_others(self):
        return self.effective_against_others

    @abstractmethod
    def get_effective_against_me(self):
        return self.effective_against_me
    
   
    
    @abstractmethod
    def get_level(self):
        return self.level
    
    @abstractmethod
    def __repr__(self):
        return "The " + self.get_pokemon_type() + " " +  self.get_name() + " of " + str(self.level) + " with " + str(self.hit_points) + " HP."

    @abstractmethod
    def get_pokemon_type(self):
        pass   

    @abstractmethod
    def get_damage(self, other):
        pass
    
    @abstractmethod
    def level_up(self, level_gain):
      pass
    
    

class Pokemon_helper(Pokemon):
    def __repr__(self):
        return "The " + self.get_pokemon_type() + " " +  self.get_name() + " of " + str(self.level) + " with " + str(self.hit_points) + " HP."
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
            self.hit_points = self.hit_points - floor((self.start_life)*0.1)
            other.absorb(self.get_damage(other))
        print("attack pok "+ self.get_type() + " " + str(self.hit_points))
        print("defend pok " + other.get_type() + " " + str(other.hit_points) + " damage " + str(a- other.hit_points))

    def can_fight(self):
        if floor(self.start_life/10)>self.hit_points:
            return False
        else:
            return True
    
    
    def get_level(self):
        return self.level
    def get_hit_points(self):
        return self.hit_points
    
    def get_defense_power(self):
        return self.defense_power
