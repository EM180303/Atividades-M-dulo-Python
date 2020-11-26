import random
import math

jogos = int(input('Quantos palpites você vai querer? '))

Ltemp = []
Palpites = []

for c in range(jogos):
    for i in range(6):
        Ltemp.append(math.ceil(60 * random.random()))

    Palpites = Ltemp[:]

print(Palpites)