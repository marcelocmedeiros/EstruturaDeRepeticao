# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
23 -Faça um programa que mostre todos os primos entre 1 e N
sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões
que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo
e o número de testes (divisões) executados.
'''

print('=' * 40)
print('{:=^40}'.format(" ' QUAIS OS PRIMOS 1-N' "))
print('=' * 40, '\n')

# entrada de variável
n = int(input('Digite um numero: '))

#contador
quant = 0
# laço repetição indicado 1 até N (soma + 1) pq range exclui o último
for i in range(1, n + 1):
    cont = 0

    # laço para conta número de divisões
    for y in range(1, i + 1):
        quant += 1
        if i % y == 0:
            cont += 1
    # condição para ser primo
    if cont <= 2:
        print(f'{i} é um número primo')

print(f'\nQuantidade de divisões {quant}')