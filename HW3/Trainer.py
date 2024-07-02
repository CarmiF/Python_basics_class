from Pokemon import Pokemon
import copy
from math import floor

class Trainer:

    def __init__(self, name, age, exp_modifier, pokemons_lst=None):

        if not isinstance(name, str):
            raise TypeError("name type wrong")
        else: 
            self.name = name

        if not isinstance(age, int):
            raise TypeError("age type wrong")
        if 16 <= age <= 120:
            self.age = age
        else: 
            raise ValueError("age must be 16 <= age <= 120")
        
        if not isinstance(float(exp_modifier), float):
            raise TypeError("exp_modifier type wrong")
        if 1.5 <= exp_modifier <= 12.5:
            self.exp_modifier = float(exp_modifier)
        else: 
            raise ValueError("exp_modifier must be 1.5 <= exp_modifier <= 12.5")
        
        self.pokemons_lst = copy.deepcopy(pokemons_lst)
        
    
    
    def __len__(self):
        return len(self.pokemons_lst)

    def __repr__(self):
        str1_to_print = ""
        if self.pokemons_lst == None:
            str_pokemon_list = ""
            str_to_print  = "The Trainer " + self.name + " is "+ str(self.age) + " years old and has the following pokemons (0 in total):"

        else: 
          
            str_to_print =  f"The Trainer {self.name} is {str(self.age)} years old and has the following pokemons ({str(len(self.pokemons_lst))} in total):"
            for i, pokemon in enumerate(self.pokemons_lst):
                str1_to_print = str1_to_print+f"\n    The {pokemon.get_type()} {str(pokemon.get_name())} of level {str(pokemon.get_level())} with {str(pokemon.get_hit_points())} HP" 

        return f"{str_to_print}{str1_to_print}"
        

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_exp_modifier(self):
        return self.exp_modifier
    
    def get_pokemon_lst(self):
        return self.pokemons_lst
    
    def change_pokemon_lst(self, pokemon, pokemon_id):
        self.pokemons_lst[pokemon_id] = pokemon
        return self
    
    def catch_pokemon(self, pokemon):
        capture_chances =(pokemon.catch_rate * self.exp_modifier * ((100-pokemon.get_hit_points())/100))
        # print(capture_chances)
        if capture_chances > 50:
            if self.pokemons_lst == None:
                self.pokemons_lst = [pokemon]
            else:
                self.add_pokemon(pokemon)
            print(self.name + " caught " + pokemon.get_name())
        else:
            print(self.name + " couldn't catch " + pokemon.get_name())

    def __eq__(self, other):
       self_hp, other_hp = self.operators_helper(other)
       if self_hp == other_hp:
           return True
       else:
           return False
           
           
    def __ne__(self, other):
       self_hp, other_hp = self.operators_helper(other)
       if self_hp != other_hp:
           return True
       else:
           return False
       
    def __gt__(self, other):
       self_hp, other_hp = self.operators_helper(other)
       if self_hp > other_hp:
           return True
       else:
           return False
       
    def __it__(self, other):
       self_hp, other_hp = self.operators_helper(other)
       if self_hp < other_hp:
           return True
       else:
           return False
       
    def __ge__(self, other):
       self_hp, other_hp = self.operators_helper(other)
    #    print( self_hp, other_hp)
       if self_hp >= other_hp:
           return True
       else:
           return False
       
    def __le__(self, other):
       self_hp, other_hp = self.operators_helper(other)
       if self_hp <= other_hp:
           return True
       else:
           return False
       
    def __iadd__(self, other):
        self = other + self
        return self

    def operators_helper(self, other):
        self_hp = 0
        other_hp = 0   
        if self.pokemons_lst== None:
            self.pokemons_lst = []         
        for pokemon in self.pokemons_lst:
            self_hp = pokemon.get_hit_points() + self_hp
        for pokemon in other.pokemons_lst:
            other_hp = pokemon.get_hit_points() + other_hp
        return self_hp, other_hp

    def add_pokemon(self, pokemon):
        pok_to_add = copy.deepcopy(pokemon)
        if self.pokemons_lst == None:
            self.pokemons_lst = [pok_to_add]
        else:
            self.pokemons_lst.append(pok_to_add)

    def __add__(self, other):
        name = other.name + "-" + self.get_name()
        age = floor((self.age + other.get_age())/2)
        exp_modifier = float(((self.exp_modifier + other.exp_modifier)/2))
        if self >= other:
            updated_pokemons_lst = self.get_pokemon_lst() + other.get_pokemon_lst()
        else:
            updated_pokemons_lst = other.get_pokemon_lst() +self.get_pokemon_lst()

       
        del self, other
        new_trainer = Trainer(name, age, exp_modifier)
        new_trainer.pokemons_lst = updated_pokemons_lst
        return new_trainer

         



