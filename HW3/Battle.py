from Trainer import Trainer
from Pokemon import Pokemon
import copy

class Battle:
    def __init__(self, __trainer1, __trainer2):
        
        if not isinstance(__trainer1, Trainer):
            raise TypeError("__trainer1 type wrong")      
        
        if not isinstance(__trainer2, Trainer):
            raise TypeError("__trainer2 type wrong")         
        self.__trainer1 = __trainer1
        self.__trainer2 = __trainer2
    

    def check_can_fight(self, pokemon1, pokemon2):
        if not pokemon1.can_fight() and not pokemon2.can_fight():
            return "draw"
            
        if not pokemon1.can_fight():
            return "pok 2 won"
            
        if not pokemon2.can_fight():
            return "pok 1 won"
        

        return "fight go on"
            

    def dual_battle(self, __trainer1_pokemon_id, __trainer2_pokemon_id):
        if len(self.__trainer1.get_pokemon_lst()) <= __trainer1_pokemon_id:
            raise ValueError("Index is bigger than __trainer1 pokemon list")
        if len(self.__trainer2.get_pokemon_lst()) <= __trainer1_pokemon_id:
            raise ValueError("Index is bigger than __trainer2 pokemon list")
        pokemon___trainer1 = self.__trainer1.get_pokemon_lst()[__trainer1_pokemon_id]
        pokemon___trainer2 = self.__trainer2.get_pokemon_lst()[__trainer2_pokemon_id]

        round_num = 0
        winning_pokemon = "fight go on"

        winning_pokemon = self.check_can_fight(pokemon___trainer1, pokemon___trainer2)
        while(winning_pokemon == "fight go on"):
            round_num = round_num +1
            pokemon___trainer1.attack(pokemon___trainer2)

            winning_pokemon = self.check_can_fight(pokemon___trainer1, pokemon___trainer2)
            if winning_pokemon != "fight go on":
                break
            pokemon___trainer2.attack(pokemon___trainer1)
            winning_pokemon = self.check_can_fight(pokemon___trainer1, pokemon___trainer2)
            if winning_pokemon != "fight go on":
                break
        if winning_pokemon == "draw":
            winning_trainer_index = 0
        elif winning_pokemon == "pok 1 won":
            winning_trainer_index = 1
        elif winning_pokemon == "pok 2 won":
            winning_trainer_index = 2
        return(round_num ,winning_trainer_index)
    
    def chose_pokemon_can_fight(self, trainer):
        for i, pokemon in enumerate(trainer.get_pokemon_lst()):
            if pokemon.can_fight():
                return pokemon, i
        return -1,-1
    
    def most_damage_pokemon(self, trainer, opponent_pok):
        if isinstance(trainer.get_pokemon_lst(), list) and isinstance(opponent_pok, Pokemon):
            if len(trainer.get_pokemon_lst())>0:
                chosen_pok, chosen_pok_index = self.chose_pokemon_can_fight(trainer)
                if isinstance(chosen_pok, Pokemon):
                    for i, pok in enumerate(trainer.get_pokemon_lst()):
                        if pok.can_fight():
                            if chosen_pok.get_damage(opponent_pok) < pok.get_damage(opponent_pok):
                                chosen_pok =pok
                                chosen_pok_index = i
                    if chosen_pok.can_fight():
                        return chosen_pok, chosen_pok_index
        return -1,-1




    def total_battle(self):
       
        round_result = 0
        win = False
        trainer_won = 0
        while win == False:
            if trainer_won == 0:
                self.__trainer1.pok1 ,pok1_i = self.chose_pokemon_can_fight(self.__trainer1)
                if isinstance(self.__trainer1.pok1, Pokemon):
                    self.__trainer2.pok2, pok2_i = self.most_damage_pokemon(self.__trainer2, self.__trainer1.pok1)
                else:
                    self.__trainer2.pok2, pok2_i = self.chose_pokemon_can_fight(self.__trainer2)
            else:
                if trainer_won == 1:
                    self.__trainer2.pok2, pok2_i = self.most_damage_pokemon(self.__trainer2, self.__trainer1.pok1)
                if trainer_won == 2:
                    self.__trainer1.pok1,pok1_i = self.most_damage_pokemon(self.__trainer1, self.__trainer2.pok2)
            if isinstance(self.__trainer1.pok1, int) and isinstance(self.__trainer2.pok2, int):
                print("The battle ended with a draw")
                return
            if isinstance(self.__trainer1.pok1, int):
                print("Trainer " + self.__trainer2.pok2.get_name() + " won the battle in  "+ str(round_result) +" rounds")
                return
            if isinstance(self.__trainer2.pok2, int):
                print("Trainer " +self.__trainer1.get_name() + " won the battle in " + str(round_result) +" rounds")
                return
            
            fight_tuple = self.dual_battle(pok1_i ,pok2_i)
            round_result = fight_tuple[0] + round_result
            trainer_won = fight_tuple[1]


        

            