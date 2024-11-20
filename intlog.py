
# functions to find the logarithm of an integer with an integer base
# finds floor(log_b(a)) without risk of floating point errors

def intLog(value, base):
    counter = 0
    while value > 0:
        value //= base
        counter += 1
    
    return counter - 1

def fastintLog(value, base):
    squares = []
    counter = 0

    k = base
    # initialize squares
    while k <= value:
        squares.append(k)
        k *= k

    # count powers
    for i in range(len(squares)-1, -1, -1):
        if squares[i] <= value:
            value //= squares[i]
            counter += 2 ** i
    return counter
