from Trainer import Trainer
from Pokemon import Pokemon
import copy

class Battle:
    def __init__(self, trainer1, trainer2):
        
        if not isinstance(trainer1, Trainer):
            raise TypeError("trainer1 type wrong")      
        
        if not isinstance(trainer2, Trainer):
            raise TypeError("trainer2 type wrong")         
        self.trainer1 = trainer1
        self.trainer2 = trainer2
    

    def check_can_fight(self, pokemon1, pokemon2):
        if not pokemon1.can_fight() and not pokemon2.can_fight():
            return "draw"
            
        if not pokemon1.can_fight():
            return "pok 2 won"
            
        if not pokemon2.can_fight():
            return "pok 1 won"
        

        return "fight go on"
            

    def dual_battle(self, trainer1_pokemon_id, trainer2_pokemon_id):
        if len(self.trainer1.get_pokemon_lst()) <= trainer1_pokemon_id:
            raise ValueError("Index is bigger than trainer1 pokemon list")
        if len(self.trainer2.get_pokemon_lst()) <= trainer1_pokemon_id:
            raise ValueError("Index is bigger than trainer2 pokemon list")
        pokemon_trainer1 = self.trainer1.get_pokemon_lst()[trainer1_pokemon_id]
        pokemon_trainer2 = self.trainer2.get_pokemon_lst()[trainer2_pokemon_id]

        round_num = 0
        winning_pokemon = "fight go on"
        while(winning_pokemon == "fight go on"):
            round_num = round_num +1
            pokemon_trainer1.attack(pokemon_trainer2)
            
            winning_pokemon = self.check_can_fight(pokemon_trainer1, pokemon_trainer2)
            if winning_pokemon != "fight go on":
                break
            pokemon_trainer2.attack(pokemon_trainer1)
            winning_pokemon = self.check_can_fight(pokemon_trainer1, pokemon_trainer2)
            if winning_pokemon != "fight go on":
                break
        print(winning_pokemon)
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
                    return chosen_pok, chosen_pok_index
        return -1,-1




    def total_battle(self):
        trainer1 = self.trainer1
        trainer2= self.trainer2
        round_result = 0
        win = False
        trainer_won = 0
        while win == False:

            if trainer_won == 0:
                pok1,pok1_i = self.chose_pokemon_can_fight(trainer1)
                if isinstance(pok1, Pokemon):
                    pok2, pok2_i = self.most_damage_pokemon(trainer2, pok1)
                else:
                    pok2, pok2_i = self.chose_pokemon_can_fight(trainer2)
            else:
                if trainer_won == 1:
                    pok2, pok2_i = self.most_damage_pokemon(trainer2, pok1)
                if trainer_won == 2:
                    pok1,pok1_i = self.most_damage_pokemon(trainer1, pok2)
            
            if isinstance(pok1, int) and isinstance(pok2, int):
                win = True
                return "The battle ended with a draw"
            if isinstance(pok1, int):
                win = True
                return trainer2.get_name() + " won the battle in  "+ str(round_result) +" rounds"
            if isinstance(pok2, int):
                win = True
                return trainer1.get_name() + " won the battle in " + str(round_result) +" rounds"
            
            fight_tuple = self.dual_battle(pok1_i ,pok2_i)
            round_result = int(fight_tuple[0]) + round_result
            trainer_won = fight_tuple[1]
            if round_result< 30:
                print(fight_tuple , round_result)


        

            