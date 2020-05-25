# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
22 -Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
'''

print('=' * 40)
print('{:=^40}'.format(" 'NÃO PRIMO' "))
print('=' * 40, '\n')

# entrada de variável
numero = int(input('Digite um numero: '))

#contador
i = 1
cont = 0

# laço de repetição para saber n° de divisões
while i <= numero:
    if numero % i == 0:
        cont += 1
    i += 1
print(f'O número {numero} tem {cont} divisões')
# condisão de ser primo
if cont <= 2:
    print(f'Por tanto o {numero} é primo')
else:
    print(f'Por tanto {numero} não é primo')
    print('Números divisíveis')
    y = 1
    # aqui vai ser informado os números multiplos
    while y <= numero:
        if numero % y == 0:
            print(y, end=' ')
        y += 1
