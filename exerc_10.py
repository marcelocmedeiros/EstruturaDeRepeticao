# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
10 - Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
'''

print('=' * 40)
print('{:=^40}'.format(" 'GERAR N° INTEIROS ENTRE DOIS NÚMEROS' "))
print('=' * 40, '\n')

num_1 = int(input('Informe o 1ª número: '))
num_2 = int(input('Informe o 2ª número: '))

# laço vai imprimir os números entre num_1 e num_2
for c in range (num_1 + 1, num_2):
    print(c, end= '-> ')