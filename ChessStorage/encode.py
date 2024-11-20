
from intlog import fastintLog

# takes in a value and a base
# returns a digit in the base, new value, and number of leading zeroes (ie # of moves to waste)

def encodeOnce(val, base):
    # if base is too low (too few moves) then make the first one
    if base <= 1:
        return 0, val, 0

    # find top digit
    # val + 0.5 to minimize float errors
    digit_pos = fastintLog(val, base)

    # find place value of top digit
    place_value = base ** digit_pos

    # find digit
    unit = val // place_value

    # subtract off the value of digit
    sub = unit * place_value
    newval = val - sub

    
    # check for new leading zeros
    lead = 0
    while True:
        place_value //= base
        if place_value < 1:
            break
        if place_value > newval:
            lead += 1
        else:
            break

    return unit, newval, lead


