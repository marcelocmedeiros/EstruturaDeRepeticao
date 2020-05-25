# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
21 -Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

print('=' * 40)
print('{:=^40}'.format(" 'NÚMERO PRIMO' "))
print('=' * 40, '\n')

# variável informada
num = int(input('Informe um número: '))
# vou contar quanta vezes o número "N" vai ter disisão exata.
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
    else:
        cont

print(f'O número que digitou foi {num} ele é divisível {cont} vezes')
# se número dividir <= 2 ele é primo
if cont == 2:
    print('Assim este número é PRIMO!')
else:
    print('Assim este número NÃO É PRIMO!')
print('=' * 40, '\n')
print('FIM!')