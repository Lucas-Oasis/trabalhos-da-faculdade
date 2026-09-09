produto_1 = 20
produto_2 = 15
produto_3 = 14.5

nome = input('Qual o seu nome? ')
print('Seja bem vindo {}'.format(nome))
print('Vamos as compras? ')

p1 = float(input('Digite a quantidade do primeiro produto: '))
p2 = float(input('Digite a quantidade do segundo produto: '))
p3 = float(input('Digite a quantidade do terceiro produto: '))

total = float((p1 * produto_1)+(p2*produto_2)+(p3*produto_3))

print('Suas compras deram: ',total)