# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 25/03/2020

'''
15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

print('=' * 40)
print('{:=^40}'.format(" 'SÉRIE DE FIBONACCI' "))
print('=' * 40, '\n')

# resolvido com laço FOR

n = int(input("Que termo deseja encontrar: "))
# somar os dois elementos anteriores
ultimo = 1
penultimo = 1

# lembrando sempre que n1 e n2 sempre é == "1"
if (n == 1) or (n == 2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(f'O termo que você deseja encontra é {termo}')

# resolvido com laço WHILE
'''n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1


if (n == 1) or (n == 2):
    print("1")
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)'''