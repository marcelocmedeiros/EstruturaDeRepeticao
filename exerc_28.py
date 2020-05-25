# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
28 -Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá
informar a quantidade de CDs e o valor para em cada um.
'''

print('=' * 40)
print('{:=^40}'.format(" 'TOTAL INVESTIDO POR UM COLECIONADOR' "))
print('=' * 40, '\n')

cds = int(input('Qual a quantidade de CDs você comprou: '))

soma = 0
for c in range(1, cds + 1):
    valor = float(input(f'Qual o valor do {c}° CD: '))
    soma += valor
media = soma / cds

print(f'O senhor comprou {cds} CDs\n'
      f'Com o valor total de R${soma:.2f}\n'
      f'A média gasta por CD foi R${media:.2f}.')