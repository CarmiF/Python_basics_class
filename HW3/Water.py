from Pokemon import Pokemon_helper
from abc import ABC, abstractmethod
import copy
class Water(Pokemon_helper):
   
   @abstractmethod
   def __init__(self, name, catch_rate,  pokemon_type):
        if not pokemon_type == "water":
            raise ValueError("pokemon_type type wrong")
        
        super().__init__( name, catch_rate)
       
        self.__type_pokemon = "water"
        self.__effective_against_me = ["electric"]
        self.__effective_against_others = ["fire"]

   def get_pokemon_type(self):
     return copy.deepcopy(self.__type_pokemon)

   def get_effective_against_others(self):
     return copy.deepcopy(self.__effective_against_others)
 
   def get_effective_against_me(self):
     return copy.deepcopy(self.__effective_against_me)
 
     
