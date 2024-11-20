

import chessing

f = open("hores.bmp", "rb")
dat = bytearray(f.read())
f.close()
val = int.from_bytes(dat)

movelist = chessing.toMoves(val)
print(len(movelist))
