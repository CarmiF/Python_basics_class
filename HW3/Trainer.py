class Trainer:

    def __init__(self, name, age, exp_modifier, pokemons_lst=None):
        self.name = name
        self.age = age
        self.exp_modifier = exp_modifier
        self.pokemons_lst = pokemons_lst
    def __len__(self):
        pass

    def __repr__(self):
        str_to_print  = "The Trainer " + self.name + "is "+ self.age + " years old and has the following pokemons ("+ len(self.pokemons_lst) + " in total):"
        for pokemon in self.pokemons_lst:
            str_to_print = str_to_print +  "The "+ pokemon.pokemon_type + pokemon.name + of level pokemon.level + "with" + pokemon.rank + "HP".

        return str_to_print
    
    def get_age(self):
        return self.age
    
    def get_pokemon_lst(self):
        return self.pokemons_lst
    
    def catch_pokemon(self, pokemon):
        pass

    def __add__(self, other):
        pass
