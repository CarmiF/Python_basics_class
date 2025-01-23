from Pokemon import Pokemon
from abc import abstractmethod
import copy


class Fire(Pokemon):

   @abstractmethod
   def __init__(self, name, catch_rate,  pokemon_type):
        if not pokemon_type == "fire":
            raise ValueError("pokemon_type type wrong")
        
        super().__init__(name, catch_rate)
       
        self.__type_pokemon = "fire"
        self.__effective_against_me = ["water"]
        self.__effective_against_others = []

   def get_pokemon_type(self):
     return copy.deepcopy(self.__type_pokemon)

   def get_effective_against_others(self):
     return copy.deepcopy(self.__effective_against_others)
 
   def get_effective_against_me(self):
     return copy.deepcopy(self.__effective_against_me)
 