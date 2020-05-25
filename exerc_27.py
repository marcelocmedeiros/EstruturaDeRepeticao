# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
27 -Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos
para cada turma. As turmas não podem ter mais de 40 alunos.
'''

print('=' * 40)
print('{:=^40}'.format(" 'NÚMERO MÉDIO DE ALUNOS POR TURMA' "))
print('=' * 40, '\n')

turmas = int(input('Qual a quantidade de turmas: '))

soma = 0
for c in range(1, turmas + 1):
    # para que a menssagem se repita caso informe < 40 alunos
    while True:
        alunos = int(input(f'{c}° turma tem quantos alunos: '))

        if alunos <= 40:
            break
        else:
            print('As turmas não podem ter mais de 40 alunos. Digite novamente.')
    soma += alunos

print(f'A escola têm {turmas} turmas\n'
      f'Com total de alunos de {soma}\n'
      f'Assim a média de alunos por turma é {soma / turmas:2}')