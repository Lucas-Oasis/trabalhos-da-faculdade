t1 = 'm'
t2 = 'v'
t3 = 'n'
turno = input(('Qual o seu turno? (M,V,N) ')).lower().replace('.','')
if turno == t1:
    print('Seja bem vindo ao turno matutino')
elif turno == t2:
    print('Seja bem vindo ao turno vespertino')
else:
    print('Seja bem vindo ao turno noturno')