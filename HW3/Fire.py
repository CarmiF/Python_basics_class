from Pokemon import Pokemon

class Fire(Pokemon):
 
  def __init__(self, name, catch_rate,  pokemon_type):
        if not pokemon_type == "fire":
            raise TypeError("pokemon_type type wrong")
        
        Pokemon.__init__(self, name, catch_rate)
       
        self.type_pokemon = "fire"
        self.effective_against_me = "water"
        self.effective_against_others = "electric"

  def get_pokemon_type(self):
     return self.type_pokemon
 
  def get_effective_against_me(self):
     return self.effective_against_me
 
  def get_effective_against_others(self):
     return self.effective_against_others
 