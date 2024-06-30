from Pokemon import Pokemon_helper
from abc import abstractmethod


class Fire(Pokemon_helper):

   @abstractmethod
   def __init__(self, name, catch_rate,  pokemon_type):
        if not pokemon_type == "fire":
            raise ValueError("pokemon_type type wrong")
        
        super().__init__(name, catch_rate)
       
        self.type_pokemon = "fire"
        self.effective_against_me = ["water"]
        self.effective_against_others = []

   def get_pokemon_type(self):
     return self.type_pokemon
 
   def get_effective_against_me(self):
     return self.effective_against_me
 
   def get_effective_against_others(self):
     return self.effective_against_others
 