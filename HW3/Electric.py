from Pokemon import Pokemon_helper
from abc import ABC, abstractmethod
import copy


class Electric(Pokemon_helper):

   @abstractmethod
   def __init__(self, name, catch_rate,  pokemon_type):
        if not pokemon_type == "electric":
            raise ValueError("pokemon_type type wrong")
        
        super().__init__(name, catch_rate)
       
        self.__type_pokemon = "electric"
        self.__effective_against_me = []
        self.__effective_against_others = ["water"]

   def get_pokemon_type(self):
     return copy.deepcopy(self.__type_pokemon)

   def get_effective_against_others(self):
     return copy.deepcopy(self.__effective_against_others)
 
   def get_effective_against_me(self):
     return copy.deepcopy(self.__effective_against_me)
 