import unittest
from random import randint

from src.core.pokeball import MasterBall, Pokeball, GreatBall, UltraBall
from src.generations.first import Pikachu
from src.core.status.constants import *


class MainPokemonCatchTestCase(unittest.TestCase):

    def test_capture_with_master_ball(self):
        pokemon = Pikachu()
        ball = MasterBall()
        was_caught = pokemon.catch_attempt(ball)

        self.assertTrue(was_caught)

    def test_capture_with_pokeball_ball(self):
        pokemon = Pikachu()
        ball = Pokeball()
        was_caught = pokemon.catch_attempt(ball)
        print(f"Was caught: {was_caught}")
        self.assertIn(was_caught, [True, False])

    def test_capture_with_great_ball(self):
        pokemon = Pikachu()
        ball = GreatBall()
        was_caught = pokemon.catch_attempt(ball)
        print(f"Was caught: {was_caught}")
        self.assertIn(was_caught, [True, False])

    def test_capture_with_ultra_ball(self):
        pokemon = Pikachu()
        ball = UltraBall()
        was_caught = pokemon.catch_attempt(ball)
        print(f"Was caught: {was_caught}")
        self.assertIn(was_caught, [True, False])


class MainStatusAffectedTestCase(unittest.TestCase):
    def test_capture_when_was_poisoned(self):
        pokemon = Pikachu()
        pokemon.status = POISONED
        ball = Pokeball()
        ball.n = randint(0, 11)
        was_caught = pokemon.catch_attempt(ball)

        self.assertTrue(was_caught)

    def test_capture_when_was_paralyzed(self):
        pokemon = Pikachu()
        pokemon.status = PARALYZED
        ball = Pokeball()
        ball.n = randint(0, 11)
        was_caught = pokemon.catch_attempt(ball)

        self.assertTrue(was_caught)

    def test_capture_when_was_asleep(self):
        pokemon = Pikachu()
        pokemon.status = ASLEEP
        ball = Pokeball()
        ball.n = randint(0, 24)
        was_caught = pokemon.catch_attempt(ball)

        self.assertTrue(was_caught)

    def test_capture_when_was_frozen(self):
        pokemon = Pikachu()
        pokemon.status = FROZEN
        ball = Pokeball()
        ball.n = randint(0, 24)
        was_caught = pokemon.catch_attempt(ball)

        self.assertTrue(was_caught)

    def test_capture_when_was_burned(self):
        pokemon = Pikachu()
        pokemon.status = BURNED
        ball = Pokeball()
        ball.n = randint(0, 11)
        was_caught = pokemon.catch_attempt(ball)

        self.assertTrue(was_caught)
