# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
26 -Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

print('=' * 40)
print('{:=^40}'.format(" 'CONTAGEM DE VOTOS' "))
print('=' * 40, '\n')

candidato1 = 0
candidato2 = 0
candidato3 = 0

n = int(input('Entre com a quantidade de eleitores: '))

for c in range(1, n + 1):
    print(f'{c} eleitor')
    print('[1]- Cadidato-1\n'
          '[2]- Cadidato-2\n'
          '[3]- Cadidato-3')
    voto = int(input('Digite seu voto: '))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print(f'Candidato 1 teve {candidato1} votos')
print(f'Candidato 2 teve {candidato2} votos')
print(f'Candidato 3 teve {candidato3} votos')