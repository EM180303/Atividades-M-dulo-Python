import math
import random
from random import Random
from test.test_import.data.unwritable import x
letras = []
frutas = []
frutas.append('laranja')
frutas.append('banana')
frutas.append('melancia')
frutas.append('uva')
frutas.append('jaca')
frutas.append('pinha')
frutas.append('goiaba')
frutas.append('manga')
frutas.append('caju')
frutas.append('abacate')

f = (math.ceil(10 * random.random()))
print('*********************************')
print('*** Jogo da Forca!***')
print('*********************************')
palavra_secreta = frutas[f]
letras_acertadas = []
for i in palavra_secreta:
    letras_acertadas.append('_')
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)

cont = 0
x = 0
ver = False
while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    x += 1

    if (chute in letras):
      
      print('Você já escreveu essa letra!')
      
      ver = True
    else:
     letras.append(chute)
     ver = False

    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
    else:
        if (ver == False):
            erros += 1
        print('Você tem ', erros, 'erros')
    enforcou = erros == 6  # teste lógico
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)
if(acertou):
    print('Boa, você ganhou!!')
else:
    print('Lamento, você perdeu!!')
    print('A palavra era : ', palavra_secreta)
print('Fim do jogo')
