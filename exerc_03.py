# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
3 - Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''


#loop infinito caso usuário o nome seja inferior a 3 letras
while True:
    nome = input('Informe seu nome: ').strip().upper()
    # condição para para o programa ou retorna a pergunta
    if len(nome) > 3:
        break
    else:
        print('Digite Novamente!')
#loop infinito caso a Idade: entre 0 e 150
while True:
    idade = int(input('Digite sua idade: '))
    if idade > 0 and idade <= 150:
        break
    else:
        print('Digite novamente.')
#loop infinito caso salário menor que zero
while True:
    salario = int(input('Informe seu salário: '))
    if salario >= 0:
        break
    else:
        print('Digite novamente.')
#loop infinito caso o Sexo não seja digitado: 'f' ou 'm';
while True:
    sexo = str(input('Digite seu sexo(F-feminino ou M-masculino): ')).strip().upper()[0]
    if sexo in 'FM':
        break
    else:
        print('Digite novamente.')
#loop infinito caso o Estado Civil não seja digitado: 's', 'c', 'v', 'd';
while True:
    estado = str(input('Digite seu estado civil(S-solteito, C-casado, V-Viúvo, D-divorciado): ')).strip().upper()[0]
    if estado in 'SCVD':
        break
    else:
        print('Digite novamente.')