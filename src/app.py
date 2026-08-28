import os
from lessons import DIVIDER, titulo, motivo_do_projeto

def limpar_terminal():

    input('\nPressione ENTER para continuar...\n')
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_opcao_numerica():

    while True:
        try:
            return int(input('Escolha uma das opções: '))
        except ValueError:
            print('\n[ERRO]: Valor digitado inválido\n')
            continue

def menu_interativo():

    titulo()
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

    print('-' * 30)

    while True:

        alternativa = ler_opcao_numerica()

        if (alternativa < 1 
        or alternativa > 7):
            print('\n[ERRO]: Escolha uma alternativa dentre as exibidas.\n')
            continue
        break

    print(f'Alternativa [{alternativa}] selecionada.')
    return alternativa

def main():

    limpar_terminal()
    motivo_do_projeto()
    while True:

        limpar_terminal()
        match menu_interativo():

            case 1:
                print(DIVIDER)
                _temp_stack = """ La France compte actuellement 
    plus de 68 millions d'habitants répartis sur son 
    territoire métropolitain et ses 
    départements d'outre-mer. 

    Cette population se caractérise par une grande diversité 
    culturelle et une espérance de vie parmi les plus 
    élevées au monde.

    Les zones urbaines, notamment autour de Paris, 
    Lyon et Marseille, concentrent une part 
    importante des habitants.

    Malgré un vieillissement démographique progressif, 
    le pays maintient une dynamique de croissance 
    grâce à un solde naturel et migratoire positif. """

                POPULATION = "\n".join(l.center(57) for l in _temp_stack.splitlines())
                print(POPULATION)
                print(DIVIDER)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass

if __name__ == '__main__':
    main()