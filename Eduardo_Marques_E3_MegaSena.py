import random
import math

jogos = int(input('Quantos palpites você vai querer? '))

Numeros= []
Palpites = []

for i in range(1, 61):
    Numeros.append(i)

for i in range(jogos):
    Palpites = random.sample((Numeros), 6) 
    print(f'Palpite {i + 1}°: ',sorted(Palpites))

