# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
42- Faça um programa que leia uma quantidade indeterminada de números positivos
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
'''

print('=' * 40)
print('{:=^40}'.format(" 'NÚMEROS POSITIVOS' "))
print('=' * 40, '\n')

n = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0

while n >= 0:
    n = int(input('Digite o número: '))
    if n >= 0 and n <= 25:
        i1 += 1
    if n >= 26 and n <= 50:
        i2 += 1
    if n >= 51 and n <= 75:
        i3 += 1
    if n >= 76 and n <= 100:
        i4 += 1

print(f'[0-25] = {i1}')
print(f'[26-50] = {i2}')
print(f'[51-75] = {i3}')
print(f'[76-100] = {i4}')