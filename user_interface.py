from constants import Constants
from egg import Egg


class UserInterface:
    """
    This is the user interface class where the game gets executed by the user
    The class consists of the menRus that the user uses to interact with their pokemon
    """

    @staticmethod
    def menu(pokeball):
        """
        This method implements the main menu for the user interaction
        :param pokeball: the origins of your pokemon, the Egg
        :return: the user's input
        """
        print(f"\nWhat would you like to do with {pokeball.get_name()}? \n")
        print(f"1. Play with {pokeball.get_name()}")
        print(f"2. Feed {pokeball.get_name()}")
        print(f"3. Check {pokeball.get_name()}'s status")
        print("4. Exit the game\n")
        return input()

    @staticmethod
    def game_menu():
        """
        This method implements the game menu. It iterates through the available games
        and displays them to the user
        :return: the choice of the user, an Int
        """
        game_list = Constants.get_game_list()
        while True:
            counter = 1
            print("\nGames: ")
            for game in game_list:
                print(f"{counter}. {game[0]}")
                counter += 1
            print("Please choose a game: ")
            choice = input()
            if not choice.isnumeric() or int(choice) > len(game_list) or int(choice) < 1:
                print("Sorry, your choice is invalid!")
                print("Choose Again: ")
            else:
                return int(choice)

    @staticmethod
    def food_menu():
        """
        This method implements the food menu. It iterates through the available food
        and displays them to the user
        :return: the choice of the user, an Int
        """
        food_list = Constants.get_food_list()
        while True:
            counter = 1
            print("\n🍽 Food:")
            for food in food_list:
                print(f"{counter}. {food}")
                counter += 1
            print("\nPlease choose a food item: ")
            choice = input()
            if not choice.isnumeric() or int(choice) > len(food_list) or int(choice) < 1:
                print("Sorry, your choice is invalid!")
                print("Choose Again: ")
            else:
                return int(choice)


def main():
    pokeball = Egg()

    answer_input = ["Y", "N", "M", "F"]
    answer_input = [answer.casefold() for answer in answer_input]

    while True:
        if isinstance(pokeball, Egg):
            print("You received a new Pokeball, would you like to see your new Pokemon? (Y/N):")
            choice = input().casefold()
            if choice == answer_input[0]:  # YES
                pokeball = pokeball.hatch()
                print("========================")
                print("You got...", Egg.intro_header_name())
                print("========================")
            elif choice == answer_input[1]:  # NO
                print("Sad to see you go. Goodbye! 👋")
                return
            else:
                print("Sorry, your choice is invalid!\n")
        else:
            choice = UserInterface.menu(pokeball)
            if choice == "1":  # game
                game_choice = UserInterface.game_menu()
                pokeball.play_game(game_choice)
            elif choice == "2":  # feed
                feed_choice = input("(F)ood or (M)edicine: ").casefold()
                if feed_choice == answer_input[2]:  # MEDICINE
                    pokeball.eat_medicine()
                elif feed_choice == answer_input[3]:  # FOOD
                    food_choice = UserInterface.food_menu()
                    pokeball.eat_food(food_choice)
            elif choice == "3":  # status check
                status = pokeball.check_status()
                if status == -1:  # checks the returned status of dead pokemon
                    pokeball = Egg()
            elif choice == "4":
                print("Thanks for playing, Goodbye! 👋")
                return


if __name__ == '__main__':
    main()
