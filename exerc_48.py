# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
48- Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
    Exemplo:
      12376489
      => 98467321
'''

print('=' * 40)
print('{:=^40}'.format(" 'NÚMERO INVERTIDO' "))
print('=' * 40, '\n')

numero = int(input('Digite um número: '))
#converteu número em strime
numero = str(numero)[::-1]
print(f'O número invertido é: {numero}')