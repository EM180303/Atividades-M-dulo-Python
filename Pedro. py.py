from random import randint
from time import sleep

j1 = 0
j2 = 0
c = 0
lista = ("Pedra", "Papel", "Tesoura")

print(' ')
jog1 = str(input('Jogador1, Insira Seu Nome: '))
print(' ')
jog2 = str(input('Jogador2, Insira Seu Nome: '))
print(' ')

while c < 3:
    Jogador1 = int(input('''Jogador 1, Escolha uma opcao para se jogar: 

    [0] Pedra
    [1] Papel
    [2] Tesoura
 
    Digite sua escolha: '''))

    print(' ')

    Jogador2 = int(input('''Jogador 2, Escolha uma opcao para se jogar: 

    [0] Pedra
    [1] Papel
    [2] Tesoura
 
    Digite sua escolha: '''))

    print("JO\n")
    sleep(1)
    print("KEN\n")
    sleep(1)
    print("POOH!!!\n")

    print("-="*20)
    print(jog2, " escolheu: {}".format(lista[Jogador2]))
    print(jog1, " escolheu: {}".format(lista[Jogador1]))
    print("-="*20)

    if Jogador2 == 0:
        if Jogador1 == 0:
            print("Empate!")
        elif Jogador1 == 1:
            print(jog1, " Venceu, ", jog2, "não foi dessa vez")
            j1 = j1 + 1
            c = c + 1
        elif Jogador1 == 2:
            print(jog2, " Venceu, ", jog1, "não foi dessa vez")
            j2 = j2 + 1
            c = c + 1
        else:
            print("Operacao invalida")

    elif Jogador2 == 1:
        if Jogador1 == 0:
            print(jog2, " Venceu, ", jog1, "não foi dessa vez")
            j2 = j2 + 1
            c = c + 1
        elif Jogador1 == 1:
            print("Empate!")
        elif Jogador1 == 2:
            print(jog1, " Venceu, ", jog2, "não foi dessa vez")
            j1 = j1 + 1
            c = c + 1
        else:
            print("Operacao invalida")
    elif Jogador2 == 2:
        if Jogador1 == 0:
            print(jog1, " Venceu, ", jog2, "não foi dessa vez")
            j1 = j1 + 1
            c = c + 1
        elif Jogador1 == 1:
            print(jog2, " Venceu, ", jog1, "não foi dessa vez")
            j2 = j2 + 1
            c = c + 1
        elif Jogador1 == 2:
            print("Empate!")
        else:
            print("Operacao invalida")
    else:
            print("Operacao invalida")
    if ((j1 ==  2) and (j1 > j2)):
     print('PARABÉNS ', jog1, 'VOCÊ É O GRANDE VENCEDOR COM ', j1, 'PONTOS!!!')
    elif((j2 == 2) and (j2>j1)):
     print('PARABÉNS ', jog2, 'VOCÊ É O GRANDE VENCEDOR COM ', j2, 'PONTOS!!!')