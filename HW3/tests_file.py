from Pokemon import Pokemon

# Attempting to create an instance of the abstract class Pokemon
try:
    pokemon = Pokemon("pikachu", 43)
except TypeError as e:
    print(e)  # Can't instantiate abstract class Pokemon with abstract methods ...

from Fire import Fire

# Attempting to create an instance of the abstract class Fire
try:
    fire = Fire("charmander", 43, "fire")
except TypeError as e:
    print(e)  # Can't instantiate abstract class Fire with abstract methods ...

from Charmander import Charmander

# Creating instances of Charmander and demonstrating some functionality
charmy = Charmander("charmy", 41, "fire", 6, 50, 54, 51)
lst = charmy.get_effective_against_me()
print(lst)  # ['water']
lst = "electric"
print(lst)  # ['electric']
print(charmy.get_effective_against_me())  # ['water']
print(charmy)  # The Charmander charmy of level 6 with 50 HP

charmy = Charmander("charmy", 41, "fire", 6, 50, 54, 51)
charmilious = Charmander("charmilious", 42, "fire", 13, 45, 55, 47)
print(charmy)  # The Charmander charmy of level 6 with 50 HP
print(charmilious)  # The Charmander charmilious of level 13 with 45 HP

print(charmilious.get_damage(charmy))  # 3
charmilious.attack(charmy)
print(charmy)  # The Charmander charmy of level 6 with 47 HP
print(charmilious)  # The Charmander charmilious of level 13 with 41 HP

evolved_charmy = charmy.level_up(5)
if evolved_charmy != None: charmy = evolved_charmy
del evolved_charmy
print(charmy)  # The Charmander charmy of level 11 with 47 HP

evolved_charmy = charmy.level_up(5)
if evolved_charmy != None: charmy = evolved_charmy
del evolved_charmy
print(charmy)  # The Charmeleon charmy of level 16 with 66 HP

from Pikachu import Pikachu
from Wartortle import Wartortle

# Creating instances of Pikachu and Wartortle and demonstrating some functionality
try:
    warty = Wartortle("warty", 43, "fire", 27, 65, 73, 90)
except ValueError as e:
    print(e)  # ValueError

warty = Wartortle("warty", 43, "water", 27, 65, 73, 90)
pika = Pikachu("pika", 40, "electric", 19, 43, 60, 70, 3)
print(pika.get_damage(warty))  # 15
print(warty.get_damage(pika))  # 5

from Trainer import Trainer

# Creating instances of Trainer and demonstrating some functionality
ash = Trainer("Ash", 18, 6.0)
ash.catch_pokemon(pika)
print(ash)  # The Trainer Ash is 18 years old and has the following pokemons (1 in total): The Pikachu pika of level 19 with 43 HP

misty = Trainer("Misty", 18, 5.5)
misty.catch_pokemon(warty)
print(misty)  # The Trainer Misty is 18 years old and has the following pokemons (1 in total): The Wartortle warty of level 27 with 65 HP

print(ash >= misty)  # False

combined_trainer = ash + misty
print(combined_trainer)  # The Trainer Misty-Ash is 18 years old and has the following pokemons (2 in total): The Wartortle warty of level 27 with 65 HP, The Pikachu pika of level 19 with 43 HP

from Charizard import Charizard

# Creating instances of Charizard and demonstrating some functionality
charzy = Charizard("charzy", 45, "fire", 36, 80, 99, 85)
brook = Trainer("Brook", 21, 4.1)
brook.catch_pokemon(charzy)
print(brook)  # The Trainer Brook is 21 years old and has the following pokemons (0 in total):

may = Trainer("May", 22, 7.3)
may.catch_pokemon(charzy)
print(may)  # The Trainer May is 22 years old and has the following pokemons (1 in total): The Charizard charzy of level 36 with 80 HP

print(may < combined_trainer)  # True

combined_trainer += may
print(combined_trainer)  # The Trainer Misty-Ash-May is 20 years old and has the following pokemons (3 in total): The Wartortle warty of level 27 with 65 HP, The Pikachu pika of level 19 with 43 HP, The Charizard charzy of level 36 with 80 HP

print(combined_trainer.get_exp_modifier())  # 6.525



from Pikachu import Pikachu
from Blastoise import Blastoise
from Trainer import Trainer
from Battle import Battle

# Creating instances of Pikachu and Blastoise
pika = Pikachu("pika", 40, "electric", 26, 90, 63, 85, 2)
blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)

# Creating Trainer instances with their respective Pokemon
ash = Trainer("ash", 18, 6.0, [pika])
misty = Trainer("misty", 18, 5.5, [blasty])

# Initiating a battle and performing a dual battle
battle = Battle(ash, misty)
battle_score = battle.dual_battle(0, 0)
print(battle_score)  # (4, 1)

print(ash)  # The Trainer ash is 18 years old and has the following pokemons (1 in total): The Pikachu pika of level 26 with 33 HP
print(misty)  # The Trainer misty is 18 years old and has the following pokemons (1 in total): The Blastoise blasty of level 37 with -2 HP

# Creating instances of more Pokemon
from Charmander import Charmander
from Charizard import Charizard
from Wartortle import Wartortle

charzy = Charizard("charzy", 45, "fire", 37, 93, 93, 82)
pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)

# Adding Pokemon to Ash's Trainer instance
ash = Trainer("ash", 18, 6.0, [charzy, pika])
print(ash)  # The Trainer ash is 18 years old and has the following pokemons (2 in total): The Charizard charzy of level 37 with 93 HP, The Pikachu pika of level 32 with 35 HP

warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)

# Adding Pokemon to Misty's Trainer instance
misty = Trainer("misty", 18, 5.5, [warty, charmy])
print(misty)  # The Trainer misty is 18 years old and has the following pokemons (2 in total): The Wartortle warty of level 30 with 78 HP, The Charmander charmy of level 15 with 57 HP

# Performing a total battle
battle = Battle(ash, misty)
battle.total_battle()
print("The battle ended with a draw")

print(misty)  # The Trainer misty is 18 years old and has the following pokemons (2 in total): The Wartortle warty of level 30 with 0 HP, The Charmander charmy of level 15 with -6 HP
print(ash)  # The Trainer ash is 18 years old and has the following pokemons (2 in total): The Charizard charzy of level 37 with -12 HP, The Pikachu pika of level 32 with 2 HP

print(charzy)  # The Charizard charzy of level 37 with 93 HP
print(pika)  # The Pikachu pika of level 32 with 35 HP

ash = Trainer("ash", 18, 6.0, [pika, charzy])
misty = Trainer("misty", 18, 5.5, [warty, charmy])
print(misty)  # The Trainer misty is 18 years old and has the following pokemons (2 in total): The Wartortle warty of level 30 with 78 HP, The Charmander charmy of level 15 with 57 HP

battle = Battle(ash, misty)
battle.total_battle()
print("Trainer ash won the battle in 5 rounds")

print(misty)  # The Trainer misty is 18 years old and has the following pokemons (2 in total): The Wartortle warty of level 30 with 3 HP, The Charmander charmy of level 15 with 5 HP
print(ash)  # The Trainer ash is 18 years old and has the following pokemons (2 in total): The Pikachu pika of level 32 with 3 HP, The Charizard charzy of level 37 with 34 HP

print(charzy)  # The Charizard charzy of level 37 with 93 HP

# Another battle configuration
from Squirtle import Squirtle
charizardious = Charizard("charizardious", 45, "fire", 37, 93, 93,82)
squirtly = Squirtle("squirtly", 41, "water", 9, 55, 49, 72)
ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
misty = Trainer("misty", 18, 5.5, [charizardious, squirtly, blasty, charmy])

# Performing another total battle
battle = Battle(misty, ash)
battle.total_battle()
print("Trainer misty won the battle in 15 rounds")

print(misty)  # The Trainer misty is 18 years old and has the following pokemons (4 in total): The Charizard charizardious of level 37 with -12 HP, The Squirtle squirtly of level 9 with 3 HP, The Blastoise blasty of level 37 with 4 HP, The Charmander charmy of level 15 with 38 HP
print(ash)  # The Trainer ash is 18 years old and has the following pokemons (4 in total): The Charmeleon charmilious of level 19 with 6 HP, The Wartortle warty of level 30 with 2 HP, The Pikachu pika of level 32 with -2 HP, The Charizard charzy of level 35 with 1 HP

ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
misty = Trainer("misty", 18, 5.5, [charizardious, squirtly, blasty, charmy])

battle = Battle(ash, misty)
battle.total_battle()
print("Trainer ash won the battle in 15 rounds")

print(misty)  # The Trainer misty is 18 years old and has the following pokemons (4 in total): The Charizard charizardious of level 37 with 5 HP, The Squirtle squirtly of level 9 with 5 HP, The Blastoise blasty of level 37 with 4 HP, The Charmander charmy of level 15 with 3 HP
print(ash)  # The Trainer ash is 18 years old and has the following pokemons (4 in total): The Charmeleon charmilious of level 19 with 5 HP, The Wartortle warty of level 30 with 30 HP, The Pikachu pika of level 32 with -5 HP, The Charizard charzy of level 35 with -2 HP

# Final battle configuration
ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
misty = Trainer("misty", 18, 5.5, [charizardious, squirtly, blasty, charmy])

battle = Battle(misty, ash)
battle.total_battle()
print("The battle ended with a draw")

print(misty)  # The Trainer misty is 18 years old and has the following pokemons (4 in total): The Charmander charmy of level 15 with 5 HP, The Wartortle warty of level 30 with -4 HP
print(ash)  # The Trainer ash is 18 years old and has the following pokemons (2 in total): The Pikachu pika of level 32 with 3 HP, The Charizard charzy of level 37 with 8 HP
