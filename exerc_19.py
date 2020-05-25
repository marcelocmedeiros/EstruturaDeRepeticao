# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

print('=' * 40)
print('{:=^40}'.format(" 'SOMA MAIOR MENOR DE UM CONJUNTO 2' "))
print('=' * 40, '\n')

# informa quanto elementos queremos para o conjunto
quantidade = int(input('Digite a quantidade de elementos do conjunto: '))

#contador i == 1
i = 1
maior = 0
menor = 0
soma = 0

# enquanto i for menor/igual a quantidade o laço pede um elemento
while i <= quantidade:
    while True:
        numero = int(input(f'Digite o {i} número: '))
        # condição para aceita o número digitado
        if numero > 0 and numero < 1000:
            break
        else:
            print('Número inválido. Digite novamente.')
     # condição de verificação de maior e menor
    if i == 1:
        menor = numero
    if numero >= maior:
        maior = numero
    if numero < menor:
        menor = numero
    # soma de todos os elementos
    soma += numero
    i += 1

print(f'O maior elemento é {maior}\n'
      f'O menor elemento é {menor}\n'
      f'A soma dos elementos é {soma}')

