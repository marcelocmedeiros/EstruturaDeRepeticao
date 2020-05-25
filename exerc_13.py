# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
13 - Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''

print('=' * 40)
print('{:=^40}'.format(" 'GERADOR DE POTÊNCIA' "))
print('=' * 40, '\n')

print("base ^ expoente:\n")
# variáveis base e expoente
base = int(input("Base: "))
expoente = int(input("Expoente: "))

# contador da repetição da base
potencia = 1

# laço da repetição
for count in range(expoente):
    potencia *= base
    count += 1

print(f'{base} ^ {expoente} = {potencia}')

# opção com while
'''print("base ^ expoente:")

base=int(input("Base: "))
expoente=int(input("Expoente: "))

potencia=1
count=1

while count <= expoente:
    potencia *= base
    count +=1

print(base,"^",expoente,"=",potencia)'''