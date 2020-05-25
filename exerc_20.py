# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
20 - Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
'''

print('=' * 40)
print('{:=^40}'.format(" 'CALCULO DO FATORIAL 2' "))
print('=' * 40, '\n')

# variável pedindo a quantos números quer calcular
quantidade = int(input('Digite a quantidade: '))

# laço FOR limitando quantidade acima indicada
for i in range(1, quantidade + 1):

    # laço WHILE vai repetir a pergunta ao n° de quantidades
    while True:
        numero = int(input('Digite o %dº número: ' % i))

        # condiciona ao valor abaixo de  16
        if numero < 16:
            break
        else:
            print('Número inválido. Digito novamente.')

    # while de realização do calculo matematico
    y = 1
    fatorial = 1
    while y <= numero:
        fatorial *= y
        y += 1

    print(fatorial)