import random
import math
from random import Random

pontuação = 0
print('*****Bem vindo!*****')
print('Ao Jogo de Craps')

pergunta = str(input('Quer ver as regras? (S para sim - N para não)'))
pergunta = pergunta.upper()
print(pergunta)
if (pergunta == 'S'):
    print('Regras:')
    print('Você jogará 2 dados; Se a soma dos 2 for = 7 ou 11, você ganhou o jogo; se for = 3, 2 ou 12, você perdeu;se não for nenhum desses, o número dos   demais serão os seu ponto, você deve tirar ele novamente para pontuar, até que você tire 7 e o  jogo encerra')

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
    print('Parabéns! Você ganhou o jogo.')
elif ((result == 2) or (result== 3) or (result == 12)):
 print('Craps')
 print('É uma pena, mas você perdeu.')
else :
   print('Para pontuar, você deve tirar:',result,' novamente.' )
   verificador = False
   while (verificador == False):
       botao = input('Digite ENTER para jogar os dados')
       dado1 = (math.ceil(6 * random.random())) 
       dado2 = (math.ceil(6 * random.random()))
       result2 = (dado1 + dado2)
       print('Primeiro dado: ',dado1)
       print('Segundo dado: ',dado2)
       print('Você tirou:',result2)
       if (result2 == result):
           pontuação += 1
           print('Você fez um ponto')
           print('Pontuação: ',pontuação)

       