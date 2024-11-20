
import random
import math
from intlog import intLog
from encode import encodeOnce

val = 1000

def getBase(n = 80):
    return random.randint(2,n)
# moves encode number based on number of moves possible

# final move encodes a zero for the previous base

def genSetup(val):
    bases = []
    digits = []
    while val > 0:
        base = getBase()
        # find top digit
        # val + 0.5 to minimize float errors
        digit_pos = intLog(val, base)

        # find place value of top digit
        place_value = base ** digit_pos

        # find digit
        unit = val // place_value

        bases.append(base)
        digits.append(unit)

        # subtract off the value of digit
        sub = unit * place_value
        newval = val - sub

        # check for new leading zeros
        while True:
            place_value //= base
            if place_value < 1:
                break
            if place_value > newval:
                newbase = getBase()
                bases.append(newbase)
                digits.append(newbase)
            else:
                break

        val = newval
    return bases,digits

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
                next_digit_pos = intLog(val, base) + 1
            
            next_digit_pos += flag
            flag = 0

            place_value = base ** next_digit_pos

            add = place_value * digit

            val += add
            #print(val, add)
    
    return val

def encode(val, n = 20):
    data = []

    while val > 0:
        base = getBase(n)
        digit, val, zeros = encodeOnce(val, base)
        data.append((digit, base))
        data += [(3,3)] * zeros
    
    return data

def dataDecode(data):
    digits = []
    bases = []
    for i in data:
        digits.append(i[0])
        bases.append(i[1])
    
    return decode(digits, bases)

K = 3000
val = 0
for i in range(K // 2):
    rand1 = random.randint(0,99)
    val += rand1
    val *= 100

val = 4752743578043760478507430257740574304584750158450275435743907589140780235425043574320572435437524305743205243057**3
dat = encode(val)
print(dat)

out = dataDecode(dat)
print(out == val)

# print(val)

# bases,digits = genSetup(val)

# print(digits, bases)
# out = decode(digits, bases)

# print(val == out)


