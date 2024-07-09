import unittest
from Charmander import Charmander
from Charmeleon import Charmeleon

class TestCharmander(unittest.TestCase):
    def setUp(self):
        self.charmy = Charmander("Charmy", 45, "fire", 5, 45, 55, 50)
        self.opponent = Charmander("Opponent", 45, "fire", 5, 45, 55, 50)

    def test_get_type(self):
        self.assertEqual(self.charmy.get_type(), "Charmander")

    def test_get_damage(self):
        damage = self.charmy.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # def test_level_up(self):
    #     self.charmy.level_up(5)
    #     self.assertEqual(self.charmy.get_level(), 10)
    #     result = self.charmy.level_up(6)
    #     self.assertIsInstance(result, Charmeleon)
    #     self.assertEqual(result.get_type(), "Charmeleon")

    # def test_evolve(self):
    #     # Instead of creating a Charmander with an invalid level, we level up a valid one
    #     self.charmy.level_up(11)  # This should evolve the Charmander
    #     self.assertEqual(self.charmy.get_level(), 15)
    #     evolved_form = self.charmy.evolve()
    #     self.assertIsInstance(evolved_form, Charmeleon)
    #     self.assertEqual(evolved_form.get_type(), "Charmeleon")

    def test_repr(self):
        expected_repr = "The Charmander Charmy of level 5 with 45 HP"
        self.assertEqual(repr(self.charmy), expected_repr)

    def test_absorb(self):
        initial_hp = self.charmy.get_hit_points()
        self.charmy.absorb(10)
        self.assertEqual(self.charmy.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.charmy.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.charmy.can_fight())
        self.charmy.absorb(50)
        self.assertFalse(self.charmy.can_fight())

    def test_get_level(self):
        self.assertEqual(self.charmy.get_level(), 5)

    def test_get_hit_points(self):
        self.assertEqual(self.charmy.get_hit_points(), 45)

    def test_get_defense_power(self):
        self.assertEqual(self.charmy.get_defense_power(), 50)

    def test_get_basic_damage(self):
        damage = self.charmy.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Charmander("InvalidCharmy", 45, "fire", 20, 45, 55, 50)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Charmander("InvalidCharmy", 45, "fire", 5, 30, 55, 50)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Charmander("InvalidCharmy", 45, "fire", 5, 45, 65, 50)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Charmander("InvalidCharmy", 45, "fire", 5, 45, 55, 60)

    def test_level_up_boundary(self):
        self.charmy.level_up(10)
        self.assertEqual(self.charmy.get_level(), 15)
        result = self.charmy.level_up(1)
        self.assertIsInstance(result, Charmeleon)
        self.assertEqual(result.get_type(), "Charmeleon")

    def test_attack_no_fight(self):
        self.charmy.absorb(50)  # Charmy can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.charmy.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)

    # def test_evolve_boundaries(self):
    #     charmy = Charmander("Charmy", 45, "fire", 15, 57, 63, 57)
    #     evolved_form = charmy.evolve()
    #     self.assertEqual(evolved_form.get_hit_points(), 57)
    #     self.assertEqual(evolved_form.get_defense_power(), 72)
    #     self.assertEqual(evolved_form.get_attack_power(), 75)

from Pikachu import Pikachu

class TestPikachu(unittest.TestCase):
    def setUp(self):
        self.pikachu = Pikachu("Pika", 45, "electric", 10, 50, 60, 45, 3)
        self.opponent = Pikachu("Opponent", 45, "electric", 10, 50, 60, 45, 3)

    def test_get_type(self):
        self.assertEqual(self.pikachu.get_type(), "Pikachu")

    def test_get_damage(self):
        damage = self.pikachu.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    def test_level_up(self):
        self.pikachu.level_up(10)
        self.assertEqual(self.pikachu.get_level(), 20)
        self.pikachu.level_up(35)
        self.assertEqual(self.pikachu.get_level(), 50)  # Level should cap at 50

    def test_repr(self):
        expected_repr = "The Pikachu Pika of level 10 with 50 HP"
        self.assertEqual(repr(self.pikachu), expected_repr)

    def test_absorb(self):
        initial_hp = self.pikachu.get_hit_points()
        self.pikachu.absorb(10)
        self.assertEqual(self.pikachu.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.pikachu.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.pikachu.can_fight())
        self.pikachu.absorb(50)
        self.assertFalse(self.pikachu.can_fight())

    def test_get_level(self):
        self.assertEqual(self.pikachu.get_level(), 10)

    def test_get_hit_points(self):
        self.assertEqual(self.pikachu.get_hit_points(), 50)

    def test_get_defense_power(self):
        self.assertEqual(self.pikachu.get_defense_power(), 45)

    def test_get_basic_damage(self):
        damage = self.pikachu.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Pikachu("InvalidPika", 45, "electric", 35, 50, 60, 45, 3)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Pikachu("InvalidPika", 45, "electric", 10, 30, 60, 45, 3)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Pikachu("InvalidPika", 45, "electric", 10, 50, 100, 45, 3)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Pikachu("InvalidPika", 45, "electric", 10, 50, 60, 100, 3)

    def test_invalid_friendship(self):
        with self.assertRaises(ValueError):
            Pikachu("InvalidPika", 45, "electric", 10, 50, 60, 45, 6)

    def test_attack_no_fight(self):
        self.pikachu.absorb(50)  # Pikachu can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.pikachu.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)

from Squirtle import Squirtle

class TestSquirtle(unittest.TestCase):
    def setUp(self):
        self.squirtle = Squirtle("Squirt", 45, "water", 10, 50, 50, 70)
        self.opponent = Squirtle("Opponent", 45, "water", 10, 50, 50, 70)

    def test_get_type(self):
        self.assertEqual(self.squirtle.get_type(), "Squirtle")

    def test_get_damage(self):
        damage = self.squirtle.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    def test_level_up(self):
        self.squirtle.level_up(3)
        self.assertEqual(self.squirtle.get_level(), 13)
        self.squirtle.level_up(5)
        self.assertEqual(self.squirtle.get_level(), 18)
        result = self.squirtle.level_up(1)
        self.assertIsInstance(result, Wartortle)  # Should evolve after level 15

    def test_repr(self):
        expected_repr = "The Squirtle Squirt of level 10 with 50 HP"
        self.assertEqual(repr(self.squirtle), expected_repr)

    def test_absorb(self):
        initial_hp = self.squirtle.get_hit_points()
        self.squirtle.absorb(10)
        self.assertEqual(self.squirtle.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.squirtle.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.squirtle.can_fight())
        self.squirtle.absorb(50)
        self.assertFalse(self.squirtle.can_fight())

    def test_get_level(self):
        self.assertEqual(self.squirtle.get_level(), 10)

    def test_get_hit_points(self):
        self.assertEqual(self.squirtle.get_hit_points(), 50)

    def test_get_defense_power(self):
        self.assertEqual(self.squirtle.get_defense_power(), 70)

    def test_get_basic_damage(self):
        damage = self.squirtle.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Squirtle("InvalidSquirt", 45, "water", 20, 50, 50, 70)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Squirtle("InvalidSquirt", 45, "water", 10, 30, 50, 70)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Squirtle("InvalidSquirt", 45, "water", 10, 50, 100, 70)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Squirtle("InvalidSquirt", 45, "water", 10, 50, 50, 100)

    def test_attack_no_fight(self):
        self.squirtle.absorb(50)  # Squirtle can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.squirtle.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)


from Charmeleon import Charmeleon

class TestCharmeleon(unittest.TestCase):
    def setUp(self):
        self.charmeleon = Charmeleon("Charry", 45, "fire", 20, 65, 70, 60)
        self.opponent = Charmeleon("Opponent", 45, "fire", 20, 65, 70, 60)

    def test_get_type(self):
        self.assertEqual(self.charmeleon.get_type(), "Charmeleon")

    def test_get_damage(self):
        damage = self.charmeleon.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    def test_level_up(self):
        self.charmeleon.level_up(5)
        self.assertEqual(self.charmeleon.get_level(), 25)
        self.charmeleon = self.charmeleon.level_up(10)
        self.assertEqual(self.charmeleon.get_level(), 35)
        self.assertIsInstance(self.charmeleon, Charizard)  # Should evolve after level 31

    def test_repr(self):
        expected_repr = "The Charmeleon Charry of level 20 with 65 HP"
        self.assertEqual(repr(self.charmeleon), expected_repr)

    def test_absorb(self):
        initial_hp = self.charmeleon.get_hit_points()
        self.charmeleon.absorb(10)
        self.assertEqual(self.charmeleon.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.charmeleon.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.charmeleon.can_fight())
        self.charmeleon.absorb(60)
        self.assertFalse(self.charmeleon.can_fight())

    def test_get_level(self):
        self.assertEqual(self.charmeleon.get_level(), 20)

    def test_get_hit_points(self):
        self.assertEqual(self.charmeleon.get_hit_points(), 65)

    def test_get_defense_power(self):
        self.assertEqual(self.charmeleon.get_defense_power(), 60)

    def test_get_basic_damage(self):
        damage = self.charmeleon.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Charmeleon("InvalidCharry", 45, "fire", 10, 65, 70, 60)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Charmeleon("InvalidCharry", 45, "fire", 20, 80, 70, 60)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Charmeleon("InvalidCharry", 45, "fire", 20, 65, 100, 60)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Charmeleon("InvalidCharry", 45, "fire", 20, 65, 70, 100)

    def test_attack_no_fight(self):
        self.charmeleon.absorb(65)  # Charmeleon can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.charmeleon.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)

from Charizard import Charizard

class TestCharizard(unittest.TestCase):
    def setUp(self):
        self.charizard = Charizard("Charry", 45, "fire", 35, 80, 90, 85)
        self.opponent = Charizard("Opponent", 45, "fire", 35, 80, 90, 85)

    def test_get_type(self):
        self.assertEqual(self.charizard.get_type(), "Charizard")

    def test_get_damage(self):
        damage = self.charizard.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    def test_level_up(self):
        self.charizard.level_up(5)
        self.assertEqual(self.charizard.get_level(), 40)
        self.charizard.level_up(15)
        self.assertEqual(self.charizard.get_level(), 50)

    def test_repr(self):
        expected_repr = "The Charizard Charry of level 35 with 80 HP"
        self.assertEqual(repr(self.charizard), expected_repr)

    def test_absorb(self):
        initial_hp = self.charizard.get_hit_points()
        self.charizard.absorb(10)
        self.assertEqual(self.charizard.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.charizard.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.charizard.can_fight())
        self.charizard.absorb(80)
        self.assertFalse(self.charizard.can_fight())

    def test_get_level(self):
        self.assertEqual(self.charizard.get_level(), 35)

    def test_get_hit_points(self):
        self.assertEqual(self.charizard.get_hit_points(), 80)

    def test_get_defense_power(self):
        self.assertEqual(self.charizard.get_defense_power(), 85)

    def test_get_basic_damage(self):
        damage = self.charizard.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Charizard("InvalidCharry", 45, "fire", 51, 80, 90, 85)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Charizard("InvalidCharry", 45, "fire", 35, 100, 90, 85)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Charizard("InvalidCharry", 45, "fire", 35, 80, 100, 85)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Charizard("InvalidCharry", 45, "fire", 35, 80, 90, 100)

    def test_attack_no_fight(self):
        self.charizard.absorb(80)  # Charizard can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.charizard.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)


import unittest
from Wartortle import Wartortle
from Blastoise import Blastoise

class TestWartortle(unittest.TestCase):
    def setUp(self):
        self.wartortle = Wartortle("Warty", 45, "water", 25, 65, 70, 85)
        self.opponent = Wartortle("Opponent", 45, "water", 25, 65, 70, 85)

    def test_get_type(self):
        self.assertEqual(self.wartortle.get_type(), "Wartortle")

    def test_get_damage(self):
        damage = self.wartortle.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    def test_level_up(self):
        self.wartortle.level_up(5)
        self.assertEqual(self.wartortle.get_level(), 30)
        self.wartortle=self.wartortle.level_up(15)
        self.assertEqual(self.wartortle.get_level(), 45)

    def test_repr(self):
        expected_repr = "The Wartortle Warty of level 25 with 65 HP"
        self.assertEqual(repr(self.wartortle), expected_repr)

    def test_absorb(self):
        initial_hp = self.wartortle.get_hit_points()
        self.wartortle.absorb(10)
        self.assertEqual(self.wartortle.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.wartortle.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.wartortle.can_fight())
        self.wartortle.absorb(65)  # Wartortle can't fight now
        self.assertFalse(self.wartortle.can_fight())

    def test_get_level(self):
        self.assertEqual(self.wartortle.get_level(), 25)

    def test_get_hit_points(self):
        self.assertEqual(self.wartortle.get_hit_points(), 65)

    def test_get_defense_power(self):
        self.assertEqual(self.wartortle.get_defense_power(), 85)

    def test_get_basic_damage(self):
        damage = self.wartortle.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Wartortle("InvalidWarty", 45, "water", 35, 65, 70, 85)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Wartortle("InvalidWarty", 45, "water", 25, 100, 70, 85)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Wartortle("InvalidWarty", 45, "water", 25, 65, 100, 85)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Wartortle("InvalidWarty", 45, "water", 25, 65, 70, 120)

    def test_attack_no_fight(self):
        self.wartortle.absorb(65)  # Wartortle can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.wartortle.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)

    # def test_evolve(self):
    #     self.assertEqual(self.wartortle.evolve(), None)  # Wartortle does not evolve until level 36

    def test_evolve_at_level_36(self):
        self.wartortle.level_up(11)  # Level up to 36
        evolved = self.wartortle.evolve()
        self.assertIsInstance(evolved, Blastoise)

from Blastoise import Blastoise

class TestBlastoise(unittest.TestCase):
    def setUp(self):
        self.blastoise = Blastoise("Blasty", 45, "water", 35, 90, 95, 105)
        self.opponent = Blastoise("Opponent", 45, "water", 35, 90, 95, 105)

    def test_get_type(self):
        self.assertEqual(self.blastoise.get_type(), "Blastoise")

    def test_get_damage(self):
        damage = self.blastoise.get_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    def test_level_up(self):
        self.blastoise.level_up(5)
        self.assertEqual(self.blastoise.get_level(), 40)
        self.blastoise.level_up(15)
        self.assertEqual(self.blastoise.get_level(), 50)

    def test_repr(self):
        expected_repr = "The Blastoise Blasty of level 35 with 90 HP"
        self.assertEqual(repr(self.blastoise), expected_repr)

    def test_absorb(self):
        initial_hp = self.blastoise.get_hit_points()
        self.blastoise.absorb(10)
        self.assertEqual(self.blastoise.get_hit_points(), initial_hp - 10)

    def test_attack(self):
        initial_hp = self.opponent.get_hit_points()
        self.blastoise.attack(self.opponent)
        self.assertLess(self.opponent.get_hit_points(), initial_hp)

    def test_can_fight(self):
        self.assertTrue(self.blastoise.can_fight())
        self.blastoise.absorb(90)
        self.assertFalse(self.blastoise.can_fight())

    def test_get_level(self):
        self.assertEqual(self.blastoise.get_level(), 35)

    def test_get_hit_points(self):
        self.assertEqual(self.blastoise.get_hit_points(), 90)

    def test_get_defense_power(self):
        self.assertEqual(self.blastoise.get_defense_power(), 105)

    def test_get_basic_damage(self):
        damage = self.blastoise.get_basic_damage(self.opponent)
        self.assertIsInstance(damage, int)
        self.assertGreater(damage, 0)

    # Additional Tests

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            Blastoise("InvalidBlasty", 45, "water", 50, 90, 95, 105)

    def test_invalid_hit_points(self):
        with self.assertRaises(ValueError):
            Blastoise("InvalidBlasty", 45, "water", 35, 100, 95, 105)

    def test_invalid_attack_power(self):
        with self.assertRaises(ValueError):
            Blastoise("InvalidBlasty", 45, "water", 35, 90, 100, 105)

    def test_invalid_defense_power(self):
        with self.assertRaises(ValueError):
            Blastoise("InvalidBlasty", 45, "water", 35, 90, 95, 120)

    def test_attack_no_fight(self):
        self.blastoise.absorb(90)  # Blastoise can't fight now
        initial_hp = self.opponent.get_hit_points()
        self.blastoise.attack(self.opponent)
        self.assertEqual(self.opponent.get_hit_points(), initial_hp)

from Pokemon import Pokemon  # Assuming Pokemon class is imported correctly
from Trainer import Trainer   # Assuming Trainer class is imported correctly
import unittest
from math import floor

class TestTrainer(unittest.TestCase):

    def setUp(self):
        # Setting up some sample pokemons for testing
        self.pokemon1 = Pokemon("Pikachu", 70, "Electric", 25, 80, 65, 60)
        self.pokemon2 = Pokemon("Bulbasaur", 60, "Grass", 20, 75, 55, 50)
        self.pokemon3 = Pokemon("Charmander", 65, "Fire", 22, 70, 60, 55)
        
        # Creating sample trainers for testing
        self.trainer1 = Trainer("Ash", 18, 3.0, [self.pokemon1, self.pokemon2])
        self.trainer2 = Trainer("Misty", 20, 2.5, [self.pokemon3])

    def test_trainer_initialization(self):
        # Test initialization with correct parameters
        self.assertEqual(self.trainer1.get_name(), "Ash")
        self.assertEqual(self.trainer1.get___age(), 18)
        self.assertAlmostEqual(self.trainer1.get_exp_modifier(), 3.0, places=1)
        self.assertEqual(len(self.trainer1), 2)  # Check number of pokemons

        # Test initialization with incorrect parameters
        with self.assertRaises(TypeError):
            Trainer(123, 18, 3.0)  # Name should be a string
        
        with self.assertRaises(ValueError):
            Trainer("Ash", 15, 3.0)  # Age should be between 16 and 120
        
        with self.assertRaises(TypeError):
            Trainer("Ash", 18, "high", [self.pokemon1])  # Exp modifier should be a float

    def test_catch_pokemon(self):
        # Test catching a pokemon with high capture chances
        new_pokemon = Pokemon("Squirtle", 65, "Water", 23, 75, 58, 52)
        self.trainer1.catch_pokemon(new_pokemon)
        self.assertIn(new_pokemon, self.trainer1.get_pokemon_lst())

        # Test catching a pokemon with low capture chances
        bad_pokemon = Pokemon("Rattata", 50, "Normal", 15, 60, 40, 35)
        self.trainer2.catch_pokemon(bad_pokemon)
        self.assertNotIn(bad_pokemon, self.trainer2.get_pokemon_lst())

    def test_comparison_operators(self):
        # Test comparison operators based on total hit points of pokemons
        self.assertTrue(self.trainer1 > self.trainer2)
        self.assertFalse(self.trainer2 < self.trainer1)
        self.assertTrue(self.trainer1 == self.trainer1)

    def test_addition_operator(self):
        # Test addition operator to combine trainers
        combined_trainer = self.trainer1 + self.trainer2
        self.assertEqual(combined_trainer.get_name(), "Misty-Ash")
        self.assertEqual(combined_trainer.get___age(), floor((20 + 18) / 2))
        self.assertAlmostEqual(combined_trainer.get_exp_modifier(), (2.5 + 3.0) / 2, places=1)
        self.assertEqual(len(combined_trainer), 3)  # Check combined pokemon count

from Pokemon import Pokemon
from Trainer import Trainer
from Battle import Battle
import unittest

class TestBattle(unittest.TestCase):

    def setUp(self):
        # Setting up the specific pokemons for testing
        # self.wartortle = Wartortle("Wartortle", 70, "Water", 25, 80, 65, 60)
        self.squirtle = Squirtle("Squirtle", 60, "Water", 20, 75, 55, 50)
        self.charmeleon = Charmeleon("Charmeleon", 65, "Fire", 22, 70, 60, 55)
        self.charmander = Charmander("Charmander", 65, "Fire", 23, 75, 58, 52)
        self.charizard = Charizard("Charizard", 55, "Fire", 18, 72, 50, 45)
        self.blastoise = Blastoise("Blastoise", 75, "Water", 30, 85, 70, 65)
        self.pikachu = Pikachu("Pikachu", 90, "Electric", 40, 95, 85, 80)

        # Creating sample trainers with different sets of pokemons for testing
        self.trainer1 = Trainer("Ash", 18, 3.0, [self.wartortle, self.charmeleon, self.charizard])
        self.trainer2 = Trainer("Misty", 20, 2.5, [self.squirtle, self.charmander, self.blastoise, self.pikachu])

        # Creating a battle instance for testing
        self.battle = Battle(self.trainer1, self.trainer2)

    def test_battle_initialization(self):
        # Test initialization with correct parameters
        self.assertEqual(self.battle._Battle__trainer1, self.trainer1)
        self.assertEqual(self.battle._Battle__trainer2, self.trainer2)

        # Test initialization with incorrect parameters
        with self.assertRaises(TypeError):
            Battle("Ash", self.trainer2)  # Should raise TypeError

    def test_check_can_fight(self):
        # Test check_can_fight method with different combinations of pokemons
        self.assertEqual(self.battle.check_can_fight(self.wartortle, self.squirtle), "fight go on")
        self.wartortle.absorb(100)  # Make Wartortle unable to fight
        self.assertEqual(self.battle.check_can_fight(self.wartortle, self.squirtle), "pok 2 won")
        self.squirtle.absorb(100)  # Make Squirtle unable to fight
        self.assertEqual(self.battle.check_can_fight(self.wartortle, self.squirtle), "draw")

        # Test with other combinations
        self.assertEqual(self.battle.check_can_fight(self.charmeleon, self.blastoise), "fight go on")
        self.assertEqual(self.battle.check_can_fight(self.charmander, self.charizard), "fight go on")
        self.charmeleon.absorb(100)  # Make Charmeleon unable to fight
        self.assertEqual(self.battle.check_can_fight(self.charmeleon, self.blastoise), "pok 2 won")
        self.assertEqual(self.battle.check_can_fight(self.charmander, self.charizard), "fight go on")
        self.blastoise.absorb(100)  # Make Blastoise unable to fight
        self.assertEqual(self.battle.check_can_fight(self.charmeleon, self.blastoise), "draw")

    def test_dual_battle(self):
        # Test dual_battle method with various Pokémon combinations
        round_num, winning_trainer_index = self.battle.dual_battle(0, 0)
        self.assertGreater(round_num, 0)
        self.assertIn(winning_trainer_index, [1, 2])

        # Additional combinations
        round_num, winning_trainer_index = self.battle.dual_battle(1, 1)
        self.assertGreater(round_num, 0)
        self.assertIn(winning_trainer_index, [1, 2])

        round_num, winning_trainer_index = self.battle.dual_battle(2, 3)
        self.assertGreater(round_num, 0)
        self.assertIn(winning_trainer_index, [1, 2])

    def test_total_battle(self):
        # Test total_battle method with trainers having specific pokemons
        self.battle.total_battle()

if __name__ == "__main__":
    unittest.main()
