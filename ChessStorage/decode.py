from intlog import fastintLog

def decode(digits, bases):
    val = 0
    flag = 0

    while len(digits) > 0:
        digit = digits.pop()
        base = bases.pop()
        
        if base <= 1:
            pass
        elif digit == base:
            flag += 1
        else:
            # get position of next digit in new base
            if val == 0:
                next_digit_pos = 0
            else:
                next_digit_pos = fastintLog(val, base) + 1
            
            next_digit_pos += flag
            flag = 0

            place_value = base ** next_digit_pos

            add = place_value * digit

            val += add
            #print(val, add)
    
    return val
