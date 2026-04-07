from bonus.bonus14 import feet_inches
from bonus.parser14 import parse


def convert(feet, inches):
    feet, inches = parse(feet_inches)
    meters = feet * 0.3048 + inches * 0.0254
    return meters
