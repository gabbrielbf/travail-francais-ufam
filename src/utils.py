import os
from lessons import titulo

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

    titulo('la france'.upper())
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

def exit_program():
    """ function that exits (or not) the program
    according to a user interaction """

    while True:
        try:

            certainty = str(input('Are you sure you want to exit?[Y/N]: ')).lower().strip()

            if certainty != 'y' and certainty != 'n': # <- Checks if the user typed something other than Y or N
                print('\n[ERROR] Only [Y/N]!')
                continue

        except ValueError:
            print('\n[ERROR] Invalid value.\n')
            continue
        break

    if certainty == 'y':
        print('\nProgram ended.\n') # <- EXITS
        return True

    elif certainty == 'n':
        print('\nThen let\'s go back!\n') # <- GOES BACK TO THE MENU

    return False