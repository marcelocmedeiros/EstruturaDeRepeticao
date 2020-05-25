# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
50- Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.
'''

print('=' * 40)
print('{:=^40}'.format(" 'H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N' "))
print('=' * 40, '\n')

n = int(input('Digite o número: '))
h = 1
for i in range(1, n + 1):
    h += h / i
print(f'H: {h:.2f}')