# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
25 -Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada.
'''

print('=' * 40)
print('{:=^40}'.format(" 'MÉDIA DE IDADE DA TURMA' "))
print('=' * 40, '\n')

# entrada de variável
n = int(input('Quantas pessoas tem na turma: '))
soma = 0
# laço
for c in range(1, n + 1):
    idade = int(input(f'Informe a idade da {c}° pessoa: '))
    soma += idade
media = soma / n
#
if media >= 0 and media <= 25:
    print(f'A média das idades é {media:.2f}, por tanto esssa turma é jovem!')
elif media >= 26 and media <= 60:
    print(f'A média das idades é {media},por tanto esssa turma é adulta!')
elif media > 60:
    print(f'A média das idades é {media},por tanto esssa turma é idosa!')



