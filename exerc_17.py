# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
'''

print('=' * 40)
print('{:=^40}'.format(" 'FATORIAL DE UM NÚMERO' "))
print('=' * 40, '\n')

# calculando com while
'''
# variável num
num = int(input('Digite o primeiro número: '))

# contador de um fatorial sempre começa com seu número
c = num

# variável f começa por 1 pois elemento neutro da multiplicação
f = 1

# enquanto c > 0
while c > 0:
    # end=' ' para todos ficaem na mesma linha junte com proximo print
    print(f'{c}',' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c -= 1
    
print(f'{f}')'''

# calculando com a função factorial
'''
#importar função factorial
from math import factorial

# variável num
num = int(input('Digite o primeiro número: '))

f = factorial(num)

print(f'O fatorial de {num} é {f}')'''

# calculando com FOR
numero = int(input("Fatorial de: ") )

# resultado começa por 1 pois elemento neutro da multiplicação
resultado = 1

# o laço vai 1 até numero+1 pq range exclui o último número
for n in range(1,numero+1):
    resultado *= n

print(resultado)
