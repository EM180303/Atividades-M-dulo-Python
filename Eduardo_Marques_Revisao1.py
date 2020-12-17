import os

intervalos = (200, 299, 300, 399, 400, 499, 500, 599, 600, 699, 700, 799, 800, 899, 900, 999, 1000)
vendedores = int(input('Qantos vendedores tem na loja? '))
salario = []
exibir = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}

for i in range(vendedores):
    temp = float(input(f'Quanto foi a venda bruta do vendedor {i + 1}? '))
    salario.append(temp)

for i in range(len(salario)):
    temp = (0.09 * salario[i])
    salario.pop(i)
    salario.insert(i, temp)
    salario[i] += 200


for cont in range(len(salario)):
    if ((salario[cont] > intervalos[0]) and (salario[cont] < intervalos[1])): 
        exibir['a'] += 1
    elif ((salario[cont] > intervalos[2]) and (salario[cont] < intervalos[3])): 
        exibir['b'] += 1
    elif ((salario[cont] > intervalos[4]) and (salario[cont] < intervalos[5])): 
        exibir['c'] += 1
    elif ((salario[cont] > intervalos[6]) and (salario[cont] < intervalos[7])): 
        exibir['d'] += 1
    elif ((salario[cont] > intervalos[8]) and (salario[cont] < intervalos[9])): 
        exibir['e'] += 1
    elif ((salario[cont] > intervalos[10]) and (salario[cont] < intervalos[11])): 
        exibir['f'] += 1
    elif ((salario[cont] > intervalos[12]) and (salario[cont] < intervalos[13])): 
        exibir['g'] += 1
    elif ((salario[cont] > intervalos[14]) and (salario[cont] < intervalos[15])): 
        exibir['h'] += 1
    elif (salario[cont] > intervalos[16]): 
        exibir['i'] += 1

os.system("cls")

for k,v in exibir.items():
    print(f'{k} = {v}')

print(salario)

