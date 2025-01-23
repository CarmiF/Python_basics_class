
from Pikachu import Pikachu
from Squirtle import Squirtle
from Charmander import Charmander
from Charizard import Charizard
from Wartortle import Wartortle
from Squirtle import Squirtle
from Blastoise import Blastoise

from Trainer import Trainer
from Battle import Battle
#     (self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):

squirtly = Squirtle("squirtly", 41, "water", 9, 55, 49, 72)
blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
charzy = Charizard("charzy", 45, "fire", 36, 80, 99, 85)
pika = Pikachu("pika", 40, "electric", 19, 43, 60, 70, 3)
warty = Wartortle("warty", 43, "water", 27, 65, 73, 90)
charmilious = Charmander("charmilious", 42, "fire", -1, 45, 55, 47)
# evolved_charmy = charmilious.level_up(5)
# squirtly.__name = "a"
# print(squirtly.get_name())
# print(squirtly.__name)

# print(squirtly.get_level())
# print(squirtly.__level)

# ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
# misty = Trainer("misty", 18, 5.5, [evolved_charmy, squirtly, blasty])
# battule = Battle(ash, misty)
# ash.pokemons_lst[3].attack(ash.pokemons_lst[3])

# print(squirtly)
# print(ash.pokemons_lst[3])
# print(misty.pokemons_lst[2])
# print(pika)
# print(warty)
# print(charmilious)
# print(evolved_charmy)

# print(battule.most_damage_pokemon(ash,charzy))

