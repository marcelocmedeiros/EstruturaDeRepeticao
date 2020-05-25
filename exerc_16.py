# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''

print('=' * 40)
print('{:=^40}'.format(" 'SÉRIE DE FIBONACCI 2' "))
print('=' * 40, '\n')

# observando a sequência termo_1 = 0 e termo)2 = 1
termo_1 = 0
termo_2 = 1
print(f'{termo_1} -> {termo_2}', end='')

# um loop até que o valor seja maior que 500
# começa pelo termo_2 pq = 1
while termo_2 < 500:
    termo_3 = termo_1 +termo_2
    print(f' -> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3

print(' -> Fim')