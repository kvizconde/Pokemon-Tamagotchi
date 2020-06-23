import random


class Constants:
    """
    This class contains the lists for food and games,
    furthermore this class also contains the static methods to get the list and their indices,
    it also contains a static generator method to generate random index values.
    Also includes an introduction heading method that returns a String of the pokemon's name and type
    """
    food_list = ["pizza 🍕", "sushi 🍣", "steak 🥩", "instant-noodles 🍜", "burger 🍔", "eggplant 🍆", "taco 🌮",
                 "ice-cream 🍦"]

    game_list = [("rock paper scissors", 10), ("hide and seek", 15), ("tag", 5), ("fortnite", 30), ("chess", 20)]

    @staticmethod
    def get_food_list():
        return Constants.food_list

    @staticmethod
    def get_game_list():
        return Constants.game_list

    @staticmethod
    def get_food_id(index):
        return Constants.food_list[index]

    @staticmethod
    def get_game_id(index):
        return Constants.game_list[index]

    @staticmethod
    def generate_random(random_index):
        """
        This static method generates a random number based on the range of parameter's length
        :param random_index: random value for index
        :return: an Int
        """
        return random.randrange(len(random_index))

    @staticmethod
    def pokemon_type_emoji(pokemon):
        """
        This static method will return an introduction name showing the pokemon's name
        along with its type i.e. thunder, fire type etc..
        :param pokemon: randomly generated pokemon
        :return: introduction heading, a String
        """
        poketype_dict = {0: 'Pikachu ⚡️', 1: 'Charmander 🔥', 2: 'Bulbasaur 🌿', 3: 'Squirtle 💦'}
        return poketype_dict.get(pokemon)
