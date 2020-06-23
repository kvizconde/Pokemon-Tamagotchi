import random

from pokemon import *


class Egg:
    """
    Egg Class
    This class handles which Pokemon to hatch in a randomize way
    """
    intro_name = ""

    def __init__(self):
        self.is_hatched = False

    def hatch(self):
        """
        A method to hatch random pokemon
        :return: a new Pokemon type
        """
        if self.is_hatched:
            return
        # will determine which pokemon gets hatched through index
        random_pokemon = random.randint(0, 3)

        Egg.intro_name = Constants.pokemon_type_emoji(random_pokemon)

        if random_pokemon == 0:
            new_pokemon = Pikachu()
        elif random_pokemon == 1:
            new_pokemon = Charmander()
        elif random_pokemon == 2:
            new_pokemon = Bulbasaur()
        else:
            new_pokemon = Squirtle()

        self.is_hatched = True
        return new_pokemon

    @staticmethod
    def intro_header_name():
        return Egg.intro_name
