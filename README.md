# ChessStorage

Stores a file (really any sequence of bits) as a series of legal chess moves by representing each move by a value in a base given by the number of possible moves in the position (minus 1). Utilizes some neat math shenanigans to allow for representing a number using an arbitrary sequence of bases.

Inspired by https://www.youtube.com/watch?v=TUtafoC4-7k and improved upon by allowing for an arbitrary base instead of only using powers of two.  

### Work in progress...

## Files
reading.py
- Reads in given file and converts to chess moves
