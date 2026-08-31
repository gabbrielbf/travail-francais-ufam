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

def main():

    galerias_franca = {
    'Capitale': 'https://depositphotos.com/br/photos/capital-da-fran%C3%A7a.html',
    'Culture': 'https://commons.wikimedia.org/wiki/Category:Culture_of_France',
    'Gastronomie': (
        'https://commons.wikimedia.org/wiki/Category:Cuisine_of_France'
    ),
    'Monuments': 'https://commons.wikimedia.org/wiki/Category:Paris',
}

    limpar_terminal()
    # motivo_do_projeto()
    while True:

        limpar_terminal()
        match menu_interativo():

            case 1:
                print(DIVIDER)
                POPULATION = """ 📌 La France compte actuellement 
plus de 68 millions d'habitants répartis 
sur son territoire métropolitain et ses 
départements d'outre-mer. 

📌 Cette population se caractérise par une grande 
diversité culturelle et une espérance de vie 
parmi les plus élevées au monde.

📌 Les zones urbaines, notamment autour de Paris, 
Lyon et Marseille, concentrent une part 
importante des habitants.

📌 Malgré un vieillissement démographique 
progressif, le pays maintient une 
dynamique de croissance grâce à un 
solde naturel et migratoire positif. """

                print(POPULATION)
                print(DIVIDER)
            case 2:
                print(DIVIDER)
                LANGUE = """ 💬 Le français est la 
langue officielle de la République française, 
régie par l'Académie française depuis 
le XVIIe siècle.

🗣️  C'est également une langue parlée sur 
les cinq continents par plus de 300 millions 
de locuteurs à travers la Francophonie.

🗯️  En France, la défense et l'enrichissement 
de la langue française sont encadrés par des lois 
spécifiques, comme la loi Toubon. """

                print(LANGUE)
                print(DIVIDER)
            case 3:
                info = galerias_franca['Capitale']
                titulo('capitale'.upper())

                CAPITALE = """ ✨🏙️  Paris, surnommée la Ville Lumière, est la 
capitale politique, économique et culturelle de la France.

• Située au cœur de la région Île-de-France, elle est 
traversée par le fleuve de la Seine qui sépare la 
Rive Gauche de la Rive Droite.

• La ville abrite les principales institutions 
gouvernementales, telles que l'Élysée et l'Assemblée 
nationale.

• Avec ses millions de touristes annuels, elle demeure 
l'une des métropoles les plus influentes et visitées 
de la planète. """

                print(CAPITALE)  
                print(
                f"\nLien vers l'image: \033]8;;{info}\033\u200bCliquez ici pour"
                f' voir la photo\033]8;;\033\\'
            )
                print(DIVIDER)
            case 4:
                info = galerias_franca['Culture']
                titulo('culture'.upper())

                CULTURE = """ 🏛️🎭 La culture française bénéficie d'un 
rayonnement mondial exceptionnel à travers son histoire, 
sa littérature, ses arts visuels et ses passions 
populaires comme le sport.

• Des figures emblématiques comme Molière, Victor Hugo, 
Monet ou Debussy ont profondément marqué le patrimoine 
artistique universel, tout comme les légendes 
du football français sur les terrains internationaux.

• Le pays investit continuellement dans la protection 
de son exception culturelle, soutenant le cinéma, 
le théâtre, la musique et les grands 
événements sportifs.

• Les musées français, à l'image du célèbre Musée 
du Louvre, accueillent des chefs-d'œuvre admirés 
par des millions de visiteurs, tandis que les 
stades de football rassemblent des foules passionnées. """

                print(CULTURE)  
                print(
                f"\nLien vers l'image: \033]8;;{info}\033\u200bCliquez ici pour"
                f' voir la photo\033]8;;\033\\'
            )
                print(DIVIDER)
            case 5:
                info = galerias_franca['Gastronomie']
                titulo('culture'.upper())

                GASTRONOMIE = """ 😋 🍽️  Reconnue comme un art de vivre 
à part entière, la gastronomie française est inscrite au 
patrimoine culturel immatériel de l'humanité par l'UNESCO.

• Elle se distingue par la qualité de ses produits du terroir, 
l'art de la table et des traditions culinaires raffinées.

• Les spécialités varient considérablement selon les régions, 
allant des fromages affinés aux vins prestigieux en 
passant par la boulangerie traditionnelle.

• Les grands chefs français continuent d'innover tout en 
préservant l'excellence des techniques classiques 
de cuisine et de pâtisserie. """
                print(GASTRONOMIE)  
                print(
                f"\nLien vers l'image: \033]8;;{info}\033\u200bCliquez ici pour"
                f' voir la photo\033]8;;\033\\'
            )
                print(DIVIDER)
            case 6:
                info = galerias_franca['Monuments']
                titulo('Monuments'.upper())

                MONUMENTS = """ 🏢 🏗 Le patrimoine monumental français témoigne 
de millénaires d'histoire, allant de l'époque gallo-romaine 
jusqu'à l'architecture contemporaine.

• La Tour Eiffel, le Château de Versailles et l'Arc de Triomphe 
figurent parmi les symboles les plus célèbres de la nation.

• Les cathédrales gothiques, telles que Notre-Dame de Paris
 ou celle de Chartres, illustrent le génie 
 architectural du Moyen Âge.

• Ces sites historiques majeurs attirent chaque année un public 
international passionné d'histoire et de belles pierres. """
                print(MONUMENTS)
                print(
                f"\nLien vers l'image: \033]8;;{info}\033\u200bCliquez ici pour"
                f' voir la photo\033]8;;\033\\'
            )
                print(DIVIDER)
            case 7:
                if exit_program() == False:
                    continue
                else:
                    break

if __name__ == '__main__':
    main()