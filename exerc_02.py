# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
2 - Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
'''


#loop infinito caso usuário digite a senha igual ao nome
while True:
    nome = input('Informe seu nome: ').strip().upper()
    senha = input('Informe senha: ').strip().upper()
    #condição para para o programa ou retorna a pergunta
    if nome != senha:
        break
    else:
        print('A senha não pode ser igual seu nome. Digite novamente!')
