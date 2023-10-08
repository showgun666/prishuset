"""
Module with helper functions for prishuset
"""
import math

# Rounding function
# value is the float number to round
# direction is a string, up, down, nearest. Determine direction of rounding
# size is an integer, determines how far to round
# return new rounded value
def rounding(value, direction, size=1):
    floor_value = math.floor(value)
    ceil_value = math.ceil(value)


    if direction == 'up':
        

    if direction == 'down':
        ...

    if direction == 'nearest':
        ...

"""
För utpriser på varor  från 0- 199 kr avrundning uppåt till jämn kr.
För utpriser 200-999 avrundning upp  eller ner till närmast jämn 5 kr
För utpriser 1000 och uppåt , avrundning upp eller ner till närmast jämn 10 kr.

Casese
1.1 ska bli 2
3 ska förbli 3

"""
# Rounds to nearest integer value
# Value is a float
# return int rounded to nearest integer value from float points to precision of 2
def roundNearest(value):
    floor_value = math.floor(value)
    ceil_value = math.ceil(value)
    
    rounded_value = 0

    # Only need first 2 digits of precision
    if ceil_value >= 100:
        ceil_value = str(cell_value)[0:2]
    
    if ceil_value >= 10:
        first_point = int(str(cell_value)[0])
        second_point = int(str(cell_value)[1])
        if second_point > 4:
            first_point += 1
        if first_point > 4:
            floor_value += 1
    return floor_value
        


    
