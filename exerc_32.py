# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
32- Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
'''

print('=' * 40)
print('{:=^40}'.format(" 'CALCULE O FATORIAL' "))
print('=' * 40, '\n')

num = int(input('Digite um número: '))
total = 1
print(f'Fatorial de: {num}')
print(f'{num}! = ', end=' ')

for c in range(num, 1, -1):
    total *= c
    print(f'{c}', end = '.')
print(f'1 = {total}')
