

# Pokémon Tamagotchi ⚡️🔥🍃💧

---



**This program is based on the widely popular tamagotchi game using Pokemon types.**



👉 The program must be executed through the `user_interface.py` module where the main menu and user interaction menus reside.

&nbsp;
&nbsp;

## UserInterface Class

This is where the magic happens. In order to play the game, user must interact with this class because it is the bridge between the user and the pokepet.



It contains the following menu methods:

- **Main Menu**

  - prompts the user what they want to do with their pokepet, such as feed, play with it, or check it's status etc.

    

- **Game Menu**

  - displays the type of games that the user can choose to play with their pokepet



- **Food Menu**
  - displays a list of food items that the user can choose to feed their pokepet



- **Main**
  - this method handles the initial setup of the game by asking the user if he/she wants to open/seee their new pokepet. Furthermore, this method also handles all the external menu methods above to display to the user.

&nbsp;
&nbsp;

## Pokemon Class:

The pokemon class is an abstract base class and it consists of all the default values for pokemons/pets who inherit this class are required to have; such as:

- **Health** - 100
- **Happiness** - 100
- **Hunger** - 0



This module implements all the required functions such as:

- Feeding Pokemon (Food/Medicine)
- Playing with Pokemon
- Checking Pokemon's status



It also includes an abstract method called ```speak()``` which gets defined in each 'Pokepet-Type' class that inherit Pokemon. **These classes are:**

- Pikachu ⚡️
- Charmander 🔥
- Bulbasaur 🍃
- Squirtle 💧

Each of the pokepet classes mentioned above implement their own set of messages that gets displayed randomly to the user. 

&nbsp;
&nbsp;

## Constants Class:

This class contains the lists for the food and games that the user's pokepets need to obtain in order to avoid getting bored/lonely and/or die from hunger.



This is done through the use of static methods that get the lists by index and matches it accordingly with the user's choices prompted in the ```UserInterface``` class.

&nbsp;
&nbsp;

## Egg Class

The Egg class contains one purpose, and that is to ```hatch()``` an egg and reveal a new random Pokemon

















