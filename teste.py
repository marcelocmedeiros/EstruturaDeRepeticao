print('Digite 0 no código para sair')
print('Especifica código Preço')
while True:
    codigo = int(input('Digite o código: '))
    if codigo == 0:
        break
    quantidade = int(input('Digite a quantidade: '))

    if codigo == 100:
        print('Cachorro Quente %d %.2f' % (codigo, quantidade * 1.20))

    if codigo == 101:
        print('Bauru Simples %d %.2f' % (codigo, quantidade * 1.30))

    if codigo == 102:
        print('Bauru com ovo %d %.2f' % (codigo, quantidade * 1.50))

    if codigo == 103:
        print('Hambúrguer %d %.2f' % (codigo, quantidade * 1.20))

    if codigo == 104:
        print('Cheeseburguer %d %.2f' % (codigo, quantidade * 1.30))

    if codigo == 105:
        print('Refrigerante %d %.2f' % (codigo, quantidade * 1.00))

print(f'O total da sua conta é ')
