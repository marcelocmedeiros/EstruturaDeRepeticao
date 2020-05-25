# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
7 - Faça um programa que leia 5 números e informe o maior número..
'''

print('=' * 40)
print('{:=^40}'.format(" 'MAIOR Nº ENTRE 5 DIGITADOS' "))
print('=' * 40, '\n')

# o maior começa do zero
maior = 0
# laço de repetição FOR pois tem um limete pré- estabelecido
for c in range (1, 6):
    num = int(input(f'Informe o {c}° número: '))
    # condição para ser maior
    if num > maior:
        maior = num
print('=' * 40)
print(f'O maior número dentre os digitados foi {maior}')
print('=' * 40)
