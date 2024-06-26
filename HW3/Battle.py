import Trainer

class Battle:
    def __init__(self, trainer1, trainer2):
        
        if isinstance(trainer1, Trainer) or isinstance(trainer2, Trainer):
            raise TypeError         
        self.trainer1 = trainer1
        self.trainer2 = trainer2
    

    def dual_fight(self, trainer1_pokemon_id, trainer2_pokemon_id):
        pass