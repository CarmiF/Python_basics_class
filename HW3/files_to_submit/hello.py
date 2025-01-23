from Trainer import Trainer
from Pokemon import Pokemon
import copy

class Battle:
    def __init__(self, __trainer1, __trainer2):
        
        if not isinstance(__trainer1, Trainer):
            raise TypeError("not good")      
        
        if not isinstance(__trainer2, Trainer):
            raise TypeError("not good")         
        self.__trainer1 = __trainer1
        self.__trainer2 = __trainer2
    

    def check_can_fight(self, pok1, pok2):
        if not pok1.can_fight() and not pok2.can_fight():
            return "draw"
        
        if not pok2.can_fight():
            return "pok1"

        if not pok1.can_fight():
            return "pok2"
            
        
        

        return "continue"
            

    def dual_battle(self, __trainer1_pok_id, __trainer2_pok_id):
        if len(self.__trainer1.get_pok_lst()) <= __trainer1_pok_id:
            raise ValueError("not good")
        if len(self.__trainer2.get_pok_lst()) <= __trainer1_pok_id:
            raise ValueError("not good")
        pok___trainer1 = self.__trainer1.get_pok_lst()[__trainer1_pok_id]
        pok___trainer2 = self.__trainer2.get_pok_lst()[__trainer2_pok_id]

        round = 0
        winning_pok = "continue"

        winning_pok = self.check_can_fight(pok___trainer1, pok___trainer2)
        while(winning_pok == "continue"):
            round = round +1
            pok___trainer1.attack(pok___trainer2)

            winning_pok = self.check_can_fight(pok___trainer1, pok___trainer2)
            if winning_pok != "continue":
                break
            pok___trainer2.attack(pok___trainer1)
            winning_pok = self.check_can_fight(pok___trainer1, pok___trainer2)
            if winning_pok != "continue":
                break
        if winning_pok == "draw":
            winner_index = 0
        elif winning_pok == "pok1":
            winner_index = 1
        elif winning_pok == "pok2":
            winner_index = 2
        return(round ,winner_index)
    
    def first_can_fight(self, trainer):
        for i, pok in enumerate(trainer.get_pok_lst()):
            if pok.can_fight():
                return pok, i
        return -1,-1
    
    def strongest_pok(self, trainer, opponent_pok):
        if isinstance(trainer.get_pok_lst(), list) and isinstance(opponent_pok, pok):
            if len(trainer.get_pok_lst())>0:
                chosen_pok, chosen_pok_index = self.first_can_fight(trainer)
                if isinstance(chosen_pok, pok):
                    for i, pok in enumerate(trainer.get_pok_lst()):
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
                self.__trainer1.pok1 ,pok1_i = self.first_can_fight(self.__trainer1)
                if isinstance(self.__trainer1.pok1, pok):
                    self.__trainer2.pok2, pok2_i = self.strongest_pok(self.__trainer2, self.__trainer1.pok1)
                else:
                    self.__trainer2.pok2, pok2_i = self.first_can_fight(self.__trainer2)
            else:
                if trainer_won == 1:
                    self.__trainer2.pok2, pok2_i = self.strongest_pok(self.__trainer2, self.__trainer1.pok1)
                if trainer_won == 2:
                    self.__trainer1.pok1,pok1_i = self.strongest_pok(self.__trainer1, self.__trainer2.pok2)
            if isinstance(self.__trainer1.pok1, int) and isinstance(self.__trainer2.pok2, int):
                print("The battle ended with a draw")
                return
            if isinstance(self.__trainer1.pok1, int):
                print("Trainer " + self.__trainer2.pok2.get_name() + " won the battle in  "+ str(round_result) +" rounds")
                return
            if isinstance(self.__trainer2.pok2, int):
                print("Trainer " +self.__trainer1.get_name() + " won the battle in " + str(round_result) +" rounds")
                return
            
            fight_result = self.dual_battle(pok1_i ,pok2_i)
            round_result = fight_result[0] + round_result
            trainer_won = fight_result[1]


        

            