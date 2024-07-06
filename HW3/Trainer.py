from Pokemon import Pokemon
import copy
from math import floor

class Trainer:

    def __init__(self, __name, __age, __exp_modifier, __pokemons_lst=None):

        if not isinstance(__name, str):
            raise TypeError("__name type wrong")
        else: 
            self.__name = __name

        if not isinstance(__age, int):
            raise TypeError("__age type wrong")
        if 16 <= __age <= 120:
            self.__age = __age
        else: 
            raise ValueError("__age must be 16 <= __age <= 120")
        
        if not isinstance(float(__exp_modifier), float):
            raise TypeError("__exp_modifier type wrong")
        if 1.5 <= __exp_modifier <= 12.5:
            self.__exp_modifier = float(__exp_modifier)
        else: 
            raise ValueError("__exp_modifier must be 1.5 <= __exp_modifier <= 12.5")
        
        self.__pokemons_lst = copy.deepcopy(__pokemons_lst)
        
    
    
    def __len__(self):
        return len(self.__pokemons_lst)

    def __repr__(self):
        str1_to_print = ""
        if self.__pokemons_lst == None:
            str_pokemon_list = ""
            str_to_print  = "The Trainer " + self.__name + " is "+ str(self.__age) + " years old and has the following pokemons (0 in total):"

        else: 
          
            str_to_print =  f"The Trainer {self.__name} is {str(self.__age)} years old and has the following pokemons ({str(len(self.__pokemons_lst))} in total):"
            for i, pokemon in enumerate(self.__pokemons_lst):
                str1_to_print = str1_to_print+f"\n    The {pokemon.get_type()} {str(pokemon.get_name())} of level {str(pokemon.get_level())} with {str(pokemon.get_hit_points())} HP" 

        return f"{str_to_print}{str1_to_print}"
        

    def get_name(self):
        return self.__name

    def get___age(self):
        return self.__age
    
    def get_exp_modifier(self):
        return self.__exp_modifier
    
    def get_pokemon_lst(self):
        return self.__pokemons_lst
    
    def change_pokemon_lst(self, pokemon, pokemon_id):
        self.__pokemons_lst[pokemon_id] = pokemon
        return self
    
    def catch_pokemon(self, pokemon):
        capture_chances =(pokemon.get_catch_rate() * self.get_exp_modifier() * ((100-pokemon.get_hit_points())/100))
        # print(capture_chances)
        if capture_chances > 50:
            if self.__pokemons_lst == None:
                self.__pokemons_lst = [pokemon]
            else:
                self.add_pokemon(pokemon)
            print(self.__name + " caught " + pokemon.get_name())
        else:
            print(self.__name + " couldn't catch " + pokemon.get_name())

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
        if self.__pokemons_lst== None:
            self.__pokemons_lst = []         
        for pokemon in self.__pokemons_lst:
            self_hp = pokemon.get_hit_points() + self_hp
        for pokemon in other.__pokemons_lst:
            other_hp = pokemon.get_hit_points() + other_hp
        return self_hp, other_hp

    def add_pokemon(self, pokemon):
        pok_to_add = copy.deepcopy(pokemon)
        if self.__pokemons_lst == None:
            self.__pokemons_lst = [pok_to_add]
        else:
            self.__pokemons_lst.append(pok_to_add)

    def __add__(self, other):
        __name = other.__name + "-" + self.get_name()
        __age = floor((self.__age + other.get___age())/2)
        __exp_modifier = float(((self.__exp_modifier + other.__exp_modifier)/2))
        if self >= other:
            updated___pokemons_lst = self.get_pokemon_lst() + other.get_pokemon_lst()
        else:
            updated___pokemons_lst = other.get_pokemon_lst() +self.get_pokemon_lst()

       
        del self, other
        new_trainer = Trainer(__name, __age, __exp_modifier)
        new_trainer.__pokemons_lst = updated___pokemons_lst
        return new_trainer

         



