# Marcelo Campos de Medeiros
# ADS UNIFIP
# Estrutura de Repetição
# 24/03/2020

'''
5 - Altere o programa anterior permitindo ao usuário informar as populações
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

print('=' * 40)
print('{:=^40}'.format(" 'TAXA DE CRESCIMENTO POPULACIONAL 2' "))
print('=' * 40, '\n')

popA=float(input('Informe a população da cidade A: '))
taxa_A=float(input('Qual a taxa de crescimento da população da cidade A: '))
popB=float(input('informe a população da cidade B: '))
taxa_B=float(input('Qual a taxa de crescimento da população da cidade B: '))
# contador de anos
ano = 0

# loop  até A ultrapasse ou iguale a população do país B
while popA < popB:
	popA = popA + ((popA*taxa_A)/100)
	popB = popB +((popB*taxa_B)/100)
	ano += 1
print('='*50)
print(f'Levará {ano} anos para população da cidade "A" ser maior que a cidade "B"')
print(f'População B--> {popB:.2f} habitantes')
print(f'População A--> {popA:.2f} habitantes')
print('='*50)