import random
import math
from random import Random
print('*****Bem vindo!*****')
print('Ao Jogo de Craps')
print('Preparado?')
botao = input('Digite ENTER para jogar os dados')
dado1 = (math.ceil(6 * random.random())) 
dado2 = (math.ceil(6 * random.random()))
result = (dado1 + dado2)
print('Primeiro dado: ',dado1)
print('Segundo dado: ',dado2)
print('Você tirou:',result)

if ((result == 7) or (result == 11)):
    print("Você é um Natural")
    print('Parabéns! Você ganhou o jogo')