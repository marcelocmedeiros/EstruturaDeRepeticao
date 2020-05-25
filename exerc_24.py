# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
24 -Faça um programa que calcule o mostre a média aritmética de N notas.
'''

print('=' * 40)
print('{:=^40}'.format(" 'MÉDIA ARITMÉTICA DE N NOTAS' "))
print('=' * 40, '\n')

# entrada de variável
n = int(input('Digite o número de notas: '))
soma = 0

for c in range(1, n + 1):
    nota = float(input(f'Entre com a {c} nota: '))
    soma += nota

print(f'A média das notas é {soma / n}')