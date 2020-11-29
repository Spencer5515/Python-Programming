# Custom Module
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):  # returns file extension + 1 of '.'
    return filename[filename.index(".") + 1:]


def roll_dice(num):  # simulates rolling dice
    return random.randint(1, num)
