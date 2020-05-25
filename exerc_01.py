# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
1 - Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido.
'''

#loop infinito caso pergunta nãe seja respondida corretamente
while True:
    nota = float(input('Diga a nota, entre 0 e 10: '))
    #condição para para o programa ou retorna a pergunta
    if nota >= 0 and nota <= 10:
        break
    else:
        print('Nota invalida. Digite novamente!')
