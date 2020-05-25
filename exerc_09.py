# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

print('=' * 40)
print('{:=^40}'.format(" 'IMPRIMIR IMPARES ENTRE 1 - 50' "))
print('=' * 40, '\n')


# laço de repetição FOR pois tem um limete pré- estabelecido
'''for c in range (1, 50, 2):

    print(c, end= '-> ')'''
# segundo metodo
for c in range (1, 50):
    if c % 2 == 1:
        print(c, end= '-> ')