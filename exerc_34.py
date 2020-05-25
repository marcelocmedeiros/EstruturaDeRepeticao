# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
34- Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo. Faça um programa que peça um número inteiro
e determine se ele é ou não um número primo.

'''

print('=' * 40)
print('{:=^40}'.format(" 'NÚMEROS PRIMOS' "))
print('=' * 40, '\n')

num = int(input('Informe um número inteiro: '))

cont = 0
for c in range(1, num + 1):
    # condição para ser primo
    if num % c == 0:
        cont += 1
if cont <= 2:
    print('É um número primo')
else:
    print('Não é um número primo')