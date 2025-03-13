'''
The five Platonic Solids are
1) Tetrahedron - 4
2) Cube - 6
3) Octahedron - 8
4) Dodecahedron - 12
5) Icosahedron - 20
'''

import math
import random
import numpy

the_dice = [[1, 0, 6], [2, 0, 8], [2, 0, 20], [1, 0, 10]]
grandtotal = 0

for i in range(0, len(the_dice)):
    rolls = []
    subtotal = 0
    for j in range(0, the_dice[i][0]):
        roll = math.floor( the_dice[i][2]*random.random() + 1 )
        rolls.append(roll)
        subtotal += roll
        j += 1
        
    print("The D" + str(the_dice[i][2]) + "'s total: " + str(subtotal))
    print(rolls)
    grandtotal += subtotal
    i += 1
print("The grand total: " + str(grandtotal) + ".")

# https://en.wikipedia.org/wiki/Platonic_solid