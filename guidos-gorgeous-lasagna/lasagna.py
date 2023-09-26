"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # minutes of prep per layer


def bake_time_remaining(elapsed_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time.

    :param number_of_layers: int - duh
    :return: int - prep time (in minutes).

    Function that takes the number of layers as arguments and returns how long 
    prep will take.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed prep and bake time.

    :param number_of_layers: int - duh
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed baking time (in minutes).

    Function that takes the actual minutes the lasagna has been in the oven and
    the number of layers as arguments and returns how long we cooked so far.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
