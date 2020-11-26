import os
import time

tabela = ('Sport', 'Náutico', 'Santa Cruz', 'Salgueiro', 'Central', 'Afogados', 'Vitória', 'Petrolina', 'América', 'Flamengo Arcoverde')

for i in range(10):
    print((i+1),'°: ',tabela[i])

time.sleep(3)
os.system("cls")

print('Os 3 primeiros são: ')
for i in range(3):
    print((i+1),'°: ',tabela[i])

time.sleep(2)
os.system("cls")

print('Os 4 últimos são: ')
for i in [6, 7, 8, 9,]:
    print((i+1),'°: ',tabela[i])  

time.sleep(2)
os.system("cls") 

print('Em ordem alfabética: ')
print(sorted(tabela))

time.sleep(2)
os.system("cls") 

print('A posição do Vitória é: ',(tabela.index('Vitória')+1),'º')

