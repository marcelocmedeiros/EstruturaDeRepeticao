# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''

print('=' * 40)
print('{:=^40}'.format(" 'IMPRIMIR DE 1 A 20' "))
print('=' * 40, '\n')

# estrutura de repetição com limite
for c in range(1, 21):
    print(c)
# end=' ' permite imprimir tudo na mesma linha
for c in range(1, 21):
    print(c, end=', ')
