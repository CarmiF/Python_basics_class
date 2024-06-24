

class Pokemon:

    def __init__(self, name, catch_rate):
        pass
        # if not isinstance(name, str) or isinstance(catch_rate, int):
        #     raise TypeError("Can't instantiate abstract class Pokemon with abstract methods __repr__, absorb, attack, can_fight, get_damage, get_defense_power, get_effective_against_me, get_effective_against_others, get_hit_points, get_pokemon_type,level_up")
        
        if not 40 <= catch_rate <= 45:
            raise ValueError
        
        self.name = name
        self.catch_rate = catch_rate

    def get_name(self):
        return self.name
    
    
    def get_catch_rate(self):
        return self.catch_rate


    def __repr__(self):
        pass
    
    def absorb(self):
        pass
    
    def attack(self):
        pass

    def can_fight(self):
        pass
    def get_damage():
        pass
    
    def get_defense_power(self):
        pass
    def get_eQective_against_me(self):
        pass
    
    def get_eQective_against_others(self): 
        pass
    
    def get_hit_points(self):
        pass

    def get_pokemon_type(self): 
      pass
    
    def level_up(self):
        pass


