import time
from abc import abstractmethod, ABC

from constants import Constants


class Pokemon(ABC):
    """
    Pokemon Class
    This class contains the basic fundamental attributes and functions of a Pokemon Tamagotchi.
    It contains the blueprint for all Pokemon Types
    """

    def __init__(self, name=""):
        """
        A Pokemon Tamagotchi that is contained inside an egg until it is hatched
        by its new trainer(user) and turns into an interactive pokemon companion.
        """
        self._health = 100  # pokemon's health level starts at 100
        self._happiness = 100  # pokemon's happiness level starts at 100
        self._hunger = 0  # pokemon's hunger level starts at 0
        self.preferred_food_indices = []
        self.preferred_game_index = -1
        self.name = name
        self._hunger_ratio = 0.1
        self._happiness_ratio = 0.1
        self._health_ratio = 0.1
        self._health_level = 50
        self._last_check_time = 0

    # GETTERS
    def get_health(self):
        """
        Gets the current health stat of pokemon
        :return: health level, an integer
        """
        return int(self._health)

    def get_happiness(self):
        """
        Gets the current happiness stat of pokemon
        :return:happiness level, an integer
        """
        return int(self._happiness)

    def get_hunger(self):
        """
        Gets the current hunger stat of pokemon
        :return:hunger level, an integer
        """
        return int(self._hunger)

    def get_name(self):
        """
        Gets the name of the pokemon
        :return:name of the pokemon, a String
        """
        return self.name

    def get_preferred_food_indices(self):
        """
        Gets the indices for the preferred food from the food list
        :return: food indices, an int
        """
        return self.preferred_food_indices

    def get_preferred_game_index(self):
        """
        Gets the index for the preferred game from the game list
        :return:preferred game index, an int
        """
        return self.preferred_game_index

    # SETTERS
    def set_health(self, health):
        self._health = health

    def set_happiness(self, happiness):
        self._happiness = happiness

    def set_hunger(self, hunger):
        self._hunger = hunger

    @abstractmethod
    def speak(self):
        """
        An abstract method that lets pokemon speak to their trainers, each pokemon
        has a list of randomly generated messages that will be implemented in each of their classes
        """
        pass

    def check_status(self):
        """
        This method allows users to check the status of their pokemon and it displays
        valuable information to the user such as the pokemon's health, happiness, and hunger
        """
        print("===================================")
        print("💬 ", end="")
        self.speak()
        if self._last_check_time == 0:  # tracks the first time user checks their pokemon
            print(f"Checking {self.get_name()}'s initial status... \n")
            print("Health:    100")
            print("Happiness: 100")
            print("Hunger:    0")
            print("===================================")
            self._last_check_time = time.time()
        else:
            time_now = time.time()
            seconds_spent = int((time_now - self._last_check_time))
            self._last_check_time = time_now

            new_happiness = self.get_happiness() - self._happiness_ratio * seconds_spent
            if new_happiness < 0:
                new_happiness = 0
            self.set_happiness(new_happiness)

            new_health = self.get_health() - self._health_ratio * seconds_spent

            # handles the condition when hunger reaches 100, the loss of health doubles
            if self.get_hunger() == 100:
                new_health -= self._health_ratio * seconds_spent

            if new_health <= 0:
                print(f"Your Pokemon {self.get_name()} just died!! ☠️")
                print("You careless bastard!!")
                return -1
            self.set_health(new_health)

            new_hunger = self.get_hunger() + self._hunger_ratio * seconds_spent
            if new_hunger > 100:
                new_hunger = 100
            self.set_hunger(new_hunger)
            print(f"{self.get_name()}'s current status...\n")
            print("Health:    ", self.get_health())
            print("Happiness: ", self.get_happiness())
            print("Hunger:    ", self.get_hunger())
            print(f"\nTime since last status checked: {seconds_spent} second(s)")
            if self.get_health() < self._health_level:
                print(f"\n{self.get_name()} is sick. Feed it some Medicine 💊\n")
            print("============================================")

    def play_game(self, choice):
        """
        This method allows users to play with their pokemon,
        it accepts a choice as an index from the game list
        :param choice: an index from the game list
        """
        game = Constants.get_game_id(choice - 1)
        points = game[1]
        print(f"{self.get_name()} is HAPPY! {self.get_name()}'s happiness increased to:", self.get_happiness())
        if choice - 1 == self.get_preferred_game_index():
            points *= 2
            print(f"That is also one of {self.get_name()}'s favorite games! Double happiness for {self.get_name()}!")
        self.set_happiness(self.get_happiness() + points)
        if self.get_happiness() > 100:
            self.set_happiness(100)

    def eat_medicine(self):
        """
        This method implements the feed function for medicine,
        the pokemon's health increases when it is fed medicine
        """
        self.set_health(self.get_health() + 20)
        print(f"(Poke-Center theme song plays in the background)... "
              f"{self.get_name()}'s health has increased!!")
        if self.get_health() > 100:
            self.set_health(100)

    def eat_food(self, choice):
        """
        This method implements the feed function for food,
        the pokemon's hunger decreases by a base amount for normal food,
        when a preferred food is given, the pokemon gets a 10% bonus to the amount of hunger that is reduced
        :param choice: an index from the food list
        """
        old_hunger = self.get_hunger()
        self.set_hunger(old_hunger - 20)
        chosen_food_index = choice - 1
        print(f"...Yummy 😋, thanks master! {self.get_name()}'s hunger has decreased!!")
        if chosen_food_index in self.get_preferred_food_indices():
            self.set_hunger(self.get_hunger() - 10)
        print(f"That is also one of {self.get_name()}'s favorite food! +10% Bonus...")
        if self.get_hunger() < 0:
            self.set_hunger(0)

    def __str__(self):
        return f"...{self.get_name()} " \
               f"has hatched...\n" \
               f"Stats > Health: {self._health}, " \
               f"Happiness: {self._happiness}, Hunger: {self._hunger} \n"


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu")
        self.preferred_game_index = 0
        self.preferred_food_indices = [1, 2, 3, 7]
        self._hunger_ratio = 0.4
        self._happiness_ratio = 0.2
        self._health_ratio = 0.1
        self._health_level = 50

    def speak(self):
        messages = ["pika peee", "pikachuuu", "pika pika", "Peeeee Kaaaaa Chuuuuu!!"]
        random_message = Constants.generate_random(messages)
        return print(messages[random_message])


class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander")
        self.preferred_game_index = 1
        self.preferred_food_indices = [0, 2, 4, 7]
        self._hunger_ratio = 0.3
        self._happiness_ratio = 0.4
        self._health_ratio = 0.25
        self._health_level = 40

    def speak(self):
        messages = ["charmaaander", "charm...charmander", "Charmander Chaaarm!!"]
        random_message = Constants.generate_random(messages)
        return print(messages[random_message])


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur")
        self.preferred_game_index = 2
        self.preferred_food_indices = [0, 5, 6, 7]
        self._hunger_ratio = 0.4
        self._happiness_ratio = 0.3
        self._health_ratio = 0.3
        self._health_level = 40

    def speak(self):
        messages = ["bulbaa bulbasaur", "bulba bulba", "Bul..Bul..Bulbaasauuuurr!!"]
        random_message = Constants.generate_random(messages)
        return print(messages[random_message])


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle")
        self.preferred_game_index = 3
        self.preferred_food_indices = [0, 3, 6, 7]
        self._hunger_ratio = 0.55
        self._happiness_ratio = 0.4
        self._health_ratio = 0.45
        self._health_level = 45

    def speak(self):
        messages = ["squirt..squirtle", "squirtle squirtle", "squirtle squirt", "Squirt...Squirtleee!!"]
        random_message = Constants.generate_random(messages)
        return print(messages[random_message])
