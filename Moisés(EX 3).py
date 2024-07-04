def vogal(escolha):
    vogais = 0
    espaco = 0
    consoantes = 0
    for letra in escolha:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra =='o' or letra == 'u':
            vogais += 1 
        elif letra == ' ':
            espaco += 1
        else:
            consoantes += 1
    print(f'a quantidade de vogal é {vogais},consoantes: {consoantes},espaço {espaco}')
desejo = 'sim'
while desejo == 'sim':
    escolha = str(input('escreva uma palavra: '))
    vogal(escolha)
    desejo = str(input('deseja continuar? '))

