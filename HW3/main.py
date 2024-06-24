
# Run example num 1
# from Pokemon import Pokemon
# pokemon = Pokemon("pikachu", 43, None)

# Run example num 2
# from Fire import Fire
# fire = Fire("charmander", 43, "fire")


# from Charmander import Charmander
# charmy = Charmander("charmy", 41, "fire", 6, 50, 54, 51)
# lst = charmy.get_effective_against_me()
# #  ['water']
# print(lst)
# # ['electric']
# charmy.get_effective_against_me()
# # ['water']
# charmy
# #  The Charmander charmy of level 6 with 50 HP



from Charmander import Charmander
charmy = Charmander("charmy", 41, "fire", 6, 50, 54, 51)
charmilious = Charmander("charmilious", 42, "fire", 13, 45, 55, 47)
print(charmy)
# The Charmander charmy of level 6 with 50 HP
print(charmilious)
# The Charmander charmilious of level 13 with 45 HP
charmilious.full_print()
charmy.full_print()
print(charmilious.get_damage(charmy))
# 3
charmilious.attack(charmy)
print(charmy)
# The Charmander charmy of level 6 with 47 HP
print(charmilious)
# The Charmander charmilious of level 13 with 41 HP
evolved_charmy = charmy.level_up(5)
if evolved_charmy != None: charmy = evolved_charmy
del evolved_charmy
print(charmy)
# The Charmander charmy of level 11 with 47 HP
evolved_charmy = charmy.level_up(5)
print(evolved_charmy)
if evolved_charmy != None: charmy = evolved_charmy
del evolved_charmy
print(charmy)
# The Charmeleon charmy of level 16 with 66 HP