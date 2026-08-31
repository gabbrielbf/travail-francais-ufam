import os
from lessons import titre

def effacer_terminal():

    input('\nAppuyez sur ENTRÉE pour continuer...\n')
    os.system('cls' if os.name == 'nt' else 'clear')

def lire_option_numerique():

    while True:
        try:
            return int(input('Choisissez une des options : '))
        except ValueError:
            print('\n[ERREUR] : Valeur saisie invalide\n')
            continue

def menu_interactif():

    titre('la france'.upper())
    options = [
        'Population',
        'Langue',
        'Capitale',
        'Culture',
        'Gastronomie',
        'Monuments',
        'Quitter'
    ]

    for indice, option in enumerate(options, start=1):
        print('{} - {}'.format(indice, option))

    print('-' * 30)

    while True:

        alternative = lire_option_numerique()

        if (alternative < 1
            or alternative > 7):
            print('\n[ERREUR] : Choisissez une alternative parmi celles affichées.\n')
            continue
        break

    print(f'Alternative [{alternative}] sélectionnée.')
    return alternative

def quitter_programme():
    """ fonction qui quitte (ou non) le programme
selon une interaction de l'utilisateur """

    while True:
        try:

            certitude = str(input('Êtes-vous sûr de vouloir quitter ?[O/N] : ')).lower().strip()

            if certitude != 'o' and certitude != 'n': # <- Vérifie si l'utilisateur a tapé autre chose que O ou N
                print('\n[ERREUR] Seulement [O/N] !')
                continue

        except ValueError:
            print('\n[ERREUR] Valeur invalide.\n')
            continue
        break

    if certitude == 'o':
        print('\nProgramme terminé.\n') # <- QUITTE
        return True

    elif certitude == 'n':
        print('\nAlors, retournons en arrière !\n') # <- RETOURNE AU MENU

    return False