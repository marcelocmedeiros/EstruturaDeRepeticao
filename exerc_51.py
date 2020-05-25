# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
51- Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
'''

print('=' * 40)
print('{:=^40}'.format(" 'S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m "))
print('=' * 40, '\n')

n = int(input('Digite o número: '))
s = 0
d = 1
for i in range(1, n + 1):
    s += i / d
    d += 2
print(f'Soma da sequência: {s:.2f}')