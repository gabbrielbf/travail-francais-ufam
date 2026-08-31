import sys, time
DIVIDER = '=' * 60

def titre(titre):

    _temp_stack = """ ----------- FR {} FR ----------- """.format(titre)
    TITRE = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)

    for char in TITRE:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

    print(DIVIDER)

def motif_du_projet():

    _temp_stack = """ J'ai utilisé mes connaissances
en programmation pour créer un petit programme
sur la France.

C'est un moyen d'améliorer mes compétences de
programmeur tout en étudiant le français."""
    MOTIF = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)

    for char in MOTIF:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

    print(DIVIDER)
    