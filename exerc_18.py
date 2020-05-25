# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
18 - Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
'''

print('=' * 40)
print('{:=^40}'.format(" 'SOMA MAIOR MENOR DE UM CONJUNTO' "))
print('=' * 40, '\n')

# informa quanto elementos queremos para o conjunto
quantidade = int(input('Digite a quantidade de elementos do conjunto: '))

#contador i == 1
i = 1
maior = 0
menor = 0
soma = 0

# enquanto i for menor/igual a quantidade o laço pede um elemento
while i <= quantidade:
    numero = int(input('Digite o elemento do conjunto: '))
    # condição comparativa de maior e menor
    if i == 1:
        menor = numero
    if numero >= maior:
        maior = numero
    if numero < menor:
        menor = numero
    # soma de todos os elementos
    soma += numero
    i += 1

print(f'O maior elemento é {maior}\n'
      f'O menor elemento é {menor}\n'
      f'A soma dos elementos é {soma}')
