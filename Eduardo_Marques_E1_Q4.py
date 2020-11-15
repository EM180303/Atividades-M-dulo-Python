import math
from test.test_import.data.unwritable import x
letras = []

print('*********************************')
print('*** Jogo da Forca!***')
print('*********************************')
palavra_secreta = 'bananas'
letras_acertadas = []
for i in palavra_secreta:
    letras_acertadas.append('_')
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)
cont = 0
cont2 = 0
ver = False
while(not enforcou and not acertou):
    chute = input("Qual letra? ")

    letras.append(chute)

    for cont in letras:
        for cont2 in cont:
         if letras[cont] == letras[cont2]:
          print('Você já escreveu essa letra!')
          ver = True

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
    print('Você ganhou!!')
else:
    print('Você perdeu!!')
print('Fim do jogo')
