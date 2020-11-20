import random
import math

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado = []
verificador = False
contador = 0
soma = 0

while (verificador == False):
    temporaria = (math.ceil(9 * random.random()))
    if (temporaria not in quadrado): 
        quadrado.append(temporaria)
        contador += 1
    if (contador == 3):
        verificador = True

for contador in range (3):
    soma += quadrado[contador] 

verificador = False
contador = 0
while (verificador == False):
    temporaria =  (math.ceil(8 * random.random()))
    print(quadrado)
    if ( temporaria not in quadrado):
        quadrado.append(numeros[temporaria])
        contador += 1  
        if (contador == 2):
            verificador = False 

print(quadrado)