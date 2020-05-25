# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero
ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

print('=' * 40)
print('{:=^40}'.format(" 'GERADOR DE TABUADA' "))
print('=' * 40, '\n')

num_1 = int(input('Informe de qual número você deseja ver a tabuada: '))

# laço vai gerar a tabuada entre 1-10
for c in range (1, 11):
    print(f'{num_1} x {c:2} = {num_1 * c:2}')
