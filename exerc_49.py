# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
49- Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
'''

print('=' * 40)
print('{:=^40}'.format(" 'S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m' "))
print('=' * 40, '\n')

numero = int(input('Informe a quantidade de termos: '))

seq, soma = 1, 0
for i in range(1, numero + 1):
    soma += i / seq
    seq += 2

print(f'Total da sequência: {soma:.2f}')