
# # Run example num 1
# from Pokemon import Pokemon
# pokemon = Pokemon("pikachu", 43, 54)

# # Run example num 2
# from Fire import Fire
# fire = Fire("charmander", 43, "fire")


# from Charmander import Charmander
# charmy = Charmander("charmy", 41, "fire", 6, 50, 54, 51)
# str = charmy.get_effective_against_me()
# print(str)
# # # #  ['water']
# print(charmy)
# # #  The Charmander charmy of level 6 with 50 HP



# from Charmander import Charmander
# charmy = Charmander("charmy", 41, "fire", 6, 50, 54, 51)
# charmilious = Charmander("charmilious", 42, "fire", 13, 45, 55, 47)
# print(charmy)
# # The Charmander charmy of level 6 with 50 HP
# print(charmilious)
# # The Charmander charmilious of level 13 with 45 HP
# charmilious.full_print()
# charmy.full_print()
# print(charmilious.get_damage(charmy))
# # # # # 3
# charmilious.attack(charmy)
# print(charmy)
# # The Charmander charmy of level 6 with 47 HP
# print(charmilious)
# # The Charmander charmilious of level 13 with 41 HP
# evolved_charmy = charmy.level_up(5)
# if evolved_charmy != None: charmy = evolved_charmy
# del evolved_charmy
# print(charmy)
# # The Charmander charmy of level 11 with 47 HP
# evolved_charmy = charmy.level_up(5)
# print(evolved_charmy)
# if evolved_charmy != None: charmy = evolved_charmy
# del evolved_charmy
# print(charmy)
# The Charmeleon charmy of level 16 with 66 HP

from Pikachu import Pikachu
from Wartortle import Wartortle
# # warty = Wartortle("warty", 43, "fire", 27, 65, 73, 90)
# # Traceback (most recent call last):
# #  raise ValueError
# # ValueError
warty = Wartortle("warty", 43, "water", 27, 65, 73, 90)
pika = Pikachu("pika", 40, "electric", 19, 43, 60, 70, 3)
# print(pika.get_damage(warty))
# # 15
# print(warty.get_damage(pika))
# # # 5
from Trainer import Trainer
ash = Trainer("Ash", 18, 6)
ash.catch_pokemon(pika)
# # Ash caught pika
print(ash)
# # The Trainer Ash is 18 years old and has the following pokemons (1 intotal):
# # The Pikachu pika of level 19 with 43 HP
misty = Trainer("Misty", 18, 5.5)
misty.catch_pokemon(warty)
# # Misty caught warty
print(misty)
# # The Trainer Misty is 18 years old and has the following pokemons (1 in
# # total):
# #  The Wartortle warty of level 27 with 65 HP
print(ash >= misty)
# # False
combined_trainer = ash + misty

print(combined_trainer)
# The Trainer Misty-Ash is 18 years old and has the following pokemons
# (2 in total):
#  The Wartortle warty of level 27 with 65 HP
#  The Pikachu pika of level 19 with 43 HP
from Charizard import Charizard
charzy = Charizard("charzy", 45, "fire", 36, 80, 99, 85)


brook = Trainer("Brook", 21, 4.1)
brook.catch_pokemon(charzy)
# Brook couldn't catch charzy
print(brook)
# # The Trainer Brook is 21 years old and has the following pokemons (0 in
# # total):
# may = Trainer("May", 22, 7.3)
# may.catch_pokemon(charzy)
# # May caught charzy
# print(may)
# # The Trainer May is 22 years old and has the following pokemons (1 in
# # total):
# #  The Charizard charzy of level 36 with 80 HP
# print(may < combined_trainer)
# # True
# combined_trainer += may
# print(combined_trainer)
# # The Trainer Misty-Ash-May is 20 years old and has the following
# # pokemons (3 in total):
# #  The Wartortle warty of level 27 with 65 HP
# #  The Pikachu pika of level 19 with 43 HP
# #  The Charizard charzy of level 36 with 80 HP
# print(combined_trainer.get_exp_modifier())
# # 6.525

# from Pikachu import Pikachu
# from Blastoise import Blastoise
# from Trainer import Trainer
# from Battle import Battle
# pika = Pikachu("pika", 40, "electric", 26, 90, 63, 85, 2)
# blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
# ash = Trainer("ash", 18, 6.0, [pika])
# misty = Trainer("misty", 18, 5.5, [blasty])
# battle = Battle(ash, misty)
# battle_score = battle.dual_fight(0, 0)
# print(battle_score)
# # (4, 1)
# print(ash)
# The Trainer ash is 18 years old and has the following pokemons (1 in
# total):
#  The Pikachu pika of level 26 with 33 HP
#  misty
# The Trainer misty is 18 years old and has the following pokemons (1 in
# total):
#  The Blastoise blasty of level 37 with -2 HP


# from Pikachu import Pikachu
# from Blastoise import Blastoise
# from Trainer import Trainer
# from Battle import Battle
# pika = Pikachu("pika", 40, "electric", 26, 90, 63, 85, 2)
# blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
# ash = Trainer("ash", 18, 6.0, [pika])
# misty = Trainer("misty", 18, 5.5, [blasty])
# battle = Battle(ash, misty)
# battle_score = battle.dual_battle(0, 0)
# battle_score
# # (4, 1)
# print(ash)
# # The Trainer ash is 18 years old and has the following pokemons (1 in
# # total):
# #  The Pikachu pika of level 26 with 33 HP
# print(misty)
# # The Trainer misty is 18 years old and has the following pokemons (1 in
# # total):
# #  The Blastoise blasty of level 37 with -2 HP


# main.py

# from Pikachu import Pikachu
# from Charmander import Charmander
# from Charizard import Charizard
# from Wartortle import Wartortle
# from Trainer import Trainer
# from Battle import Battle

# # Creating Pokemon instances
# charzy = Charizard("charzy", 45, "fire", 37, 93, 93, 82)
# pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)

# # Creating Trainer ash with their Pokemon
# ash = Trainer("ash", 18, 6.0, [charzy, pika])
# print(ash)

# # Creating more Pokemon instances
# warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
# charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)

# # Creating Trainer misty with their Pokemon
# misty = Trainer("misty", 18, 5.5, [warty, charmy])
# print(misty)

# # Performing a battle between ash and misty
# battle = Battle(ash, misty)
# print(battle.total_battle())

# # Display the state of the trainers after the battle
# print(misty)
# print(ash)

# # Reinitializing Trainers for another battle
# ash = Trainer("ash", 18, 6.0, [pika, charzy])
# misty = Trainer("misty", 18, 5.5, [warty, charmy])
# print(misty)
# print(ash)

# # Performing another battle between misty and ash
# battle = Battle(ash, misty)
# print(battle.total_battle())

# # Display the state of the trainers after the battle
# print(misty)
# print(ash)

# # Reinitializing Trainers for another battle
# ash = Trainer("ash", 18, 6.0, [pika, charzy])
# misty = Trainer("misty", 18, 5.5, [charmy, warty])

# # Performing the final battle between misty and ash
# battle = Battle(misty, ash)
# print(battle.total_battle())

# # Display the state of the trainers after the final battle
# print(misty)
# print(ash)





# # main.py

# from Pikachu import Pikachu
# from Charmander import Charmander
# from Charmeleon import Charmeleon
# from Charizard import Charizard
# from Squirtle import Squirtle
# from Wartortle import Wartortle
# from Blastoise import Blastoise
# from Trainer import Trainer
# from Battle import Battle

# # Creating Pokemon instances
# charmilious = Charmeleon("charmilious", 42, "fire", 19, 60, 71, 68)
# warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
# pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)
# charzy = Charizard("charzy", 45, "fire", 35, 95, 94, 83)

# # Creating Trainer ash with their Pokemon
# ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
# print(ash)

# # Creating more Pokemon instances
# charizardious = Charizard("charizardious", 45, "fire", 37, 93, 93, 82)
# squirtly = Squirtle("squirtly", 41, "water", 9, 55, 49, 72)
# blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
# charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)

# # Creating Trainer misty with their Pokemon
# misty = Trainer("misty", 18, 5.5, [charizardious, squirtly, blasty, charmy])
# print(misty)

# # Performing a battle between ash and misty
# battle = Battle(misty, ash)
# print(battle.total_battle())

# # Display the state of the trainers after the battle
# print(misty)
# print(ash)

# # Reinitializing Trainers for another battle
# ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
# misty = Trainer("misty", 18, 5.5, [charizardious, squirtly, blasty, charmy])

# # Performing another battle between ash and misty
# battle = Battle(ash, misty)
# print(battle.total_battle())

# # Display the state of the trainers after the battle
# print(misty)
# print(ash)
