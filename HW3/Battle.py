from Trainer import Trainer

class Battle:
    def __init__(self, trainer1, trainer2):
        
        if not isinstance(trainer1, Trainer):
            raise TypeError("trainer1 type wrong")      
        
        if not isinstance(trainer2, Trainer):
            raise TypeError("trainer2 type wrong")         
        self.trainer1 = trainer1
        self.trainer2 = trainer2
    

    def check_can_fight(self, pokemon1, pokemon2):
        if not pokemon1.can_fight() and not pokemon1.can_fight():
            return 0
            
        if not pokemon1.can_fight():
            return 2
            
        if not pokemon2.can_fight():
            return 1
        return -1
            

    def dual_fight(self, trainer1_pokemon_id, trainer2_pokemon_id):
        if len(self.trainer1.get_pokemon_lst()) <= trainer1_pokemon_id:
            raise ValueError("Index is bigger than trainer1 pokemon list")
        if len(self.trainer2.get_pokemon_lst()) <= trainer1_pokemon_id:
            raise ValueError("Index is bigger than trainer2 pokemon list")
        pokemon_trainer1 = self.trainer1.get_pokemon_lst()[trainer1_pokemon_id]
        pokemon_trainer2 = self.trainer2.get_pokemon_lst()[trainer2_pokemon_id]

        round_num = 0
        winning_pokemon = -1
        while(winning_pokemon == -1):
            round_num = round_num +1
            pokemon_trainer1.attack(pokemon_trainer2)
            winning_pokemon = self.check_can_fight(pokemon_trainer1, pokemon_trainer2)
            if winning_pokemon != -1:
                break
            pokemon_trainer2.attack(pokemon_trainer1)
            winning_pokemon = self.check_can_fight(pokemon_trainer2, pokemon_trainer1)
        
        return(winning_pokemon, round_num)

            