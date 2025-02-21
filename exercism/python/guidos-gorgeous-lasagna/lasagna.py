"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME   = 0

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """    
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the bake time remaining.

    :param number_of_layers: int - you want to add to the lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number_of_layers you want to add to the lasagna as 
    an argument and returns how many minutes you would spend making them. 
    Assume each layer takes 2 minutes to prepare..
    """
    PREPARATION_TIME = number_of_layers * 2
    return PREPARATION_TIME
    


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    :param number_of_layers: int - the number of layers added to the lasagna
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking in the oven
    :return: int - result time - (in minutes) the sum of your preparation time and the time the lasagna has already spent baking in the oven.

    Function that takes two parameters as arguments: number_of_layers (the number of layers added to the lasagna) and
    elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). 
    This function should return the total number of minutes you have been cooking, 
    or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    """    
    result = number_of_layers * 2 + elapsed_bake_time
    return result
    


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)