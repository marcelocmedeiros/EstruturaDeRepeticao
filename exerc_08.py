# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

print('=' * 40)
print('{:=^40}'.format(" 'IMPRIMIR DE 1 A 20' "))
print('=' * 40, '\n')

# soma e media
soma = media = 0
# laço de repetição FOR pois tem um limete pré- estabelecido
for c in range (1, 6):
    num = int(input(f'Informe o {c}° número: '))
    # condição para ser maior
    soma += num
media = soma / 5
print('=' * 40)
print(f'A soma entre os números é {soma}\n'
      f'A sua média foi {media}')
print('=' * 40)