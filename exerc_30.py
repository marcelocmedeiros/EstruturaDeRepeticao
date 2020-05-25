# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
30- O Sr. Manoel Joaquim acaba de adquirir uma panificadora
e pretende implantar a metodologia da tabelinha, que já é
um sucesso na sua loja de 1,99. Você foi contratado para desenvolver
o programa que monta a tabela de preços de pães, de 1 até 50 pães,
a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ...
    50 - R$ 9.00
'''

print('=' * 40)
print('{:=^40}'.format(" 'TABELA DE PREÇOS 2' "))
print('=' * 40, '\n')

preco = float(input('Digite o preço do pão: '))
print(f'Preço do pão: R$ {preco:.2f}')
# variavel indicada vai servir comoum contador para imprimir a tabela 1-50
valor = preco

print('PANIFICADORA - Tabela de preços')
# tabela 1-50
for c in range(1, 51):
    print(f'{c} - R$ {valor:.2f}')
    valor += preco


