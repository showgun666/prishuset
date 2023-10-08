"""
Module with helper functions for prishuset
"""
import sys

# Rounding function
# value is the float number to round
# direction is a string, up, down, nearest. Determine direction of rounding
# size is an integer, determines how far to round in whole numbers
# return new rounded value
def rounding(value, direction, size=1):
    rounded_value = value

    if direction == 'up':
        rounded_value = int(value // 1) + size - int(value // 1) % size

    elif direction == 'down':
        rounded_value = int(value // 1) - int(value // 1) % size

    elif direction == 'nearest':
        # Control that we are not rounding to a larger value than the current value
        if len(str(roundNearest(value))) >= len(str(size)):
            rounded_value = roundNearest(value)
            if rounded_value % size >= size / 2:
                rounded_value +=  size - rounded_value % size
            else:
                rounded_value -= rounded_value % size
        else:
            print("Selected size: " + size + "\nis larger than value: " + value + "\nexiting program")
            sys.exit()
    
    else:
        print("Invalid direction: " + direction + "\nexiting program")
        sys.exit()
    

    return rounded_value


"""

115.76
116


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
    if isinstance(value, float):
        number, floatpoints = str(value).split('.')
    else:
        number = value
        floatpoints = -1
    number = int(number)
    floatpoints = int(floatpoints)

    # Only need first 2 digits of precision
    # If ceiling value is greater or equal to 100 then strip all digits except the first two digits
    if floatpoints >= 100:
        floatpoints = int(str(floatpoints)[0:2])
    
    # If ceiling value is greater than or equal to 10
    # If second digit is greater than 4 then increase value of first digit by 1
    # If first digit is greater than 4 then increase floor value by 1
    if floatpoints >= 10:
        first_point = int(str(floatpoints)[0])
        second_point = int(str(floatpoints)[1])

        # If second digit is equal to or greater than 5 then increase value of first digit by 1
        if second_point >= 5:
            first_point += 1
        # If first digit is equal to or greater than 5 then increase floor value by 1
        if first_point >= 5:
            number += 1

    # If only one digit, if it is 5 or greater then increase value of floor value by 1
    elif floatpoints > 4:
        number += 1

    return number
