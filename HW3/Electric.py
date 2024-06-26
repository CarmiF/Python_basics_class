from Pokemon import Pokemon

class Electric(Pokemon):
 
  def __init__(self, name, catch_rate,  pokemon_type):
        if not pokemon_type == "electric":
            raise ValueError("pokemon_type type wrong")
        
        Pokemon.__init__(self, name, catch_rate)
       
        self.type_pokemon = "electric"
        self.effective_against_me = "fire"
        self.effective_against_others = "water"

  def get_pokemon_type(self):
     return self.type_pokemon
 
  def get_effective_against_me(self):
     return self.effective_against_me
 
  def get_effective_against_others(self):
     return self.effective_against_others
 
  def get_effective_against_me(self):
      return self.effective_against_me
 