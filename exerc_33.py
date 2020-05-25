# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
33- O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
'''

print('=' * 40)
print('{:=^40}'.format(" 'PROGRAMA QUE LEIA TEMPERATURAS' "))
print('=' * 40, '\n')

num = int(input('Quantas temperaturas vai informar: '))

maior = 0
menor = 0
soma = 0
for c in range(1, num +1):
    temp = float(input(f'Qual a {c}° temperatura: '))
    soma += temp
    if c == 1:
        maior = temp
        menor = temp
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
print(f'A maior temperatura é {maior}\n'
      f'A menor temperatua é {menor}\n'
      f'A média da temperatuta é {soma / num}')
