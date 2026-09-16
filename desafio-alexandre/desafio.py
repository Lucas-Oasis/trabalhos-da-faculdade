sim = 0
não = 0

Sim = 0
Não = 0

s = 0
n = 0

SIM = 0
NAO = 0

print('Um homem foi morto na última madrugada')
print('A policia começa a fazer as investigações')
print('Você será interrogado...')

pergunta_1 = input('Telefonou para a vítima? ').lower()
if pergunta_1 == 'sim':
    sim += 1
else:
    não += 1
pergunta_2 = input('Esteve no local do crime? ').lower()
if pergunta_2 == 'sim':
    sim += 1
else:
    não += 1
pergunta_3 = input('Mora perto da vítima? ').lower()
if pergunta_3 == 'sim':
    sim += 1
else:
    não += 1
pergunta_4 = input('Devia para a vítima? ').lower()
if pergunta_4 == 'sim':
    sim += 1
else:
    não += 1
pergunta_5 = input('Já trabalhou com a vítima? ').lower()
if pergunta_5 == 'sim':
    sim += 1
else:
    não += 1

if sim >= 2 and sim < 3:
    print('Você é suspeito.')
elif sim >= 3 and sim <= 4:
    print('Você é cúmplice.')
elif sim == 5:
    print('Você é o assassino.')
else:
    print('Você é inocente')
