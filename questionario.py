perguntas = [
    {'pergunta': 'Quantos dedos temos?',
     'opções':['5','10','20'],
     'resposta': '20', 
    },
    {'pergunta' : 'Quantos litros devemos beber por dia?',
     'opções' : ['2','3','5'],
     'resposta': '2',
    },
]
for pergunta in perguntas:
    print('pergunta:', pergunta['pergunta'])
    print()
   
    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()
    
    escolha = input('escolha uma opção: ')

    acertou = False
    escolha_int = None
    hmo = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < hmo:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True
    if acertou:
        hmo += 1
        print('acertou')
    else:
        print('errou')

    print()

print(f'você acertou {hmo}')  
print('de', len(perguntas), 'perguntas') 