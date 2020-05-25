# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
11 - Altere o programa anterior para mostrar no final a soma dos números.
'''

print('=' * 40)
print('{:=^40}'.format(" 'GERAR N° INTEIROS ENTRE DOIS NÚMEROS' "))
print('=' * 40, '\n')

num_1 = int(input('Informe o 1ª número: '))
num_2 = int(input('Informe o 2ª número: '))
#contador soma
soma = 0

# laço vai somar os números entre num_1 e num_2
for c in range (num_1 + 1, num_2):
    soma += c
print(f'A soma dos números que estão entre "{num_1}" e "{num_2}" é igual a "{soma}"')
