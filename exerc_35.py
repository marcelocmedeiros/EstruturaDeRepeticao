# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
35- Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário.
'''

print('=' * 40)
print('{:=^40}'.format(" 'LISTA DOS NÚMEROS PRIMOS' "))
print('=' * 40, '\n')

numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    cont = 0
    for y in range(1, i + 1):
        if i % y == 0:
            cont += 1
    if cont == 2:
        print(f'{i}', end=' ')

