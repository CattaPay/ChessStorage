import chess
import random
import encode
from decode import decode

def listLegalMoves(b: chess.Board):
    return list(b.legal_moves)

def getBase(b: chess.Board):
    return b.legal_moves.count() - 1

def whichMove(moves, move):
    for i in range(len(moves)):
        if moves[i] == move:
            return i
    return None

def dataDecode(data):
    digits = []
    bases = []
    for i in data:
        digits.append(i[0])
        bases.append(i[1])
    
    return decode(digits, bases)

def toMoves(val):
    played_moves = []
    counter = 0
    b = chess.Board()
    while val > 0:
        #print(b)
        counter += 1
        if counter % 100 == 0:
            print(counter)
        base = getBase(b)
        moves = listLegalMoves(b)

        # encode next move
        digit, val, lead = encode.encodeOnce(val, base)
        b.push(moves[digit])

        # reset board if game is over
        if b.is_game_over():
            played_moves += b.move_stack
            b = chess.Board()

        # resolve next moves
        while lead > 0:
            base = getBase(b)
            moves = listLegalMoves(b)
            if base <= 1:
                b.push(moves[0])
                if b.is_game_over():
                    played_moves += b.move_stack
                    b = chess.Board()
            else:
                b.push(moves[-1])
                lead -= 1
                if b.is_game_over():
                    played_moves += b.move_stack
                    b = chess.Board()
                

    played_moves += b.move_stack
    return played_moves

def fromMoves(moves):
    decode_board = chess.Board()
    data = []
    for i in moves:
        base = getBase(decode_board)
        moves = listLegalMoves(decode_board)
        digit = whichMove(moves, i)
        data.append((digit, base))
        decode_board.push(i)
        if decode_board.is_game_over():
            decode_board = chess.Board()
    return dataDecode(data)

