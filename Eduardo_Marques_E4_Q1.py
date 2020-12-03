import os
import time
import random
import math
from typing import Container

jokenpo = []
jokenpo.append('x')
jokenpo.append('Pedra')
jokenpo.append('Papel')
jokenpo.append('Tesoura')
escolha = []
escolha.append('x')
escolha.insert(2, 0)
rodada = []
rodada.append(0)
rodada.append(0)
rodada.append(0)
vencedor = False

print('***Bem vindos!***')
print('Preparados para o Jokenpo? Sim?')
# para que o nome do jogador 1 fique na lista com o indice 1 e o nome do jogador 2 no 2

nome = str(input('Então informe o nome do jogador : '))

print('\n Quem vencer 2  rodadas primeiro ganha')

time.sleep(2)
os.system("cls")

while (vencedor == False):
     
    for i in [1, 2, 3]:
        print('Digite ',i,' para escolher ',jokenpo[i])
    escolha.insert(1, int(input()))
    print('Você escolheu ',jokenpo[escolha[1]])

    time.sleep(2)
    os.system("cls")

    def jog_comput(jogada):
        jogada = math.ceil(3 * random.random())
        return 'O computador esoclheu',jokenpo[jogada]

    print(jog_comput(escolha[2]))

    time.sleep(2)
    os.system("cls")

    if (escolha[1] == escolha[2]):
     print('Empate')
     time.sleep(2)
     os.system("cls")
     rodada[0]+= 1
    elif (((escolha[1] == 1) and (escolha[2] == 3)) or ((escolha[1] == 2) and (escolha[2] == 1)) or ((escolha[1] == 3) and (escolha[2] == 2))): 
     print(nome,' ganhou essa rodada')
     time.sleep(2)
     os.system("cls")
     rodada[1] += 1
     rodada[0]+= 1
    elif (((escolha[2] == 1) and (escolha[1] == 3)) or ((escolha[2] == 2) and (escolha[1] == 1)) or ((escolha[2] == 3) and (escolha[1] == 2))): 
     print('Computador ganhou essa rodada')
     time.sleep(2)
     os.system("cls")
     rodada[2] += 1
     rodada[0] += 1

    if ((rodada[1] == 2) or (rodada[2] == 2)):
      vencedor = True
    else:
      vencedor = False

os.system("cls")

if(rodada[1] > rodada[2]):
    print('O vencedor foi ',nome)
    print('Placar: ')
    print(nome,': ',rodada[1],' X computador : ',rodada[2])
    print('Quantidade de rodadas: ',rodada[0])
else:
    print('O vencedor foi o computador')
    print('Placar: ')
    print(nome,': ',rodada[1],' X computador : ',rodada[2])
    print('Quantidade de rodadas: ',rodada[0])
