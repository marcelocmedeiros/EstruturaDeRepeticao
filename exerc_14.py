# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
14 - Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares
 e a quantidade de números impares.
'''

print('=' * 40)
print('{:=^40}'.format(" '10 NÚMEROS INTEIROS MOSTRE PAR & ÍMPAR' "))
print('=' * 40, '\n')

# contador de par e impar
par = 0
impar =0

# laço da repetição para repetir a pergunta
for c in range(1, 11):
    num = int(input(f'Informe o {c}º número: '))
    if  c % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Quantidade de números pares é = {par}\n'
      f'Quantidade de números impares é = {impar}')