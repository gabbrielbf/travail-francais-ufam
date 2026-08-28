
def ler_opcao_numerica():

    while True:
        try:
            return int(input('Escolha uma das opções: '))
        except ValueError:
            print('\n[ERRO]: Valor digitado inválido\n')
            continue

def menu_interativo():

    opcoes = [
        'Population',
        'Langue',
        'Capitale',
        'Culture',
        'Gastronomie',
        'Monuments',
        'Quitter'
    ]

    for indice, opcao in enumerate(opcoes, start=1):
        print('{} - {}'.format(indice, opcao))

    while True:

        alternativa = ler_opcao_numerica()

        if (alternativa < 1 
        or alternativa > 7):
            print('\n[ERRO]: Escolha uma alternativa dentre as exibidas.\n')
            continue
        break

    return alternativa