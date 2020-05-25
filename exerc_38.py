# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
38- Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    a - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
    ao dobro do percentual do ano anterior. Faça um programa que determine
    o salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.
'''

print('=' * 40)
print('{:=^40}'.format(" 'AUMENTO SALARIAL' "))
print('=' * 40, '\n')

salario = 1000
aumento = 1.5
ano = 1996

for i in range(ano, 2021):
    print(f'Salário no ano {i} = {salario:.2f}, aumento de {aumento:.2f}')
    salario += ((salario * aumento) / 100)
    aumento *= 2

print(f'Salário atual: {salario:.2f}')