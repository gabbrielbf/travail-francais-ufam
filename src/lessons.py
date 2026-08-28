import sys, time
DIVIDER = '=' * 60

def titulo(titulo):

    _temp_stack = """ ----------- 🇫🇷 {titulo} 🇫🇷 ---------- """.format(titulo)
    TITULO = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)
        
    for char in TITULO: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

    print(DIVIDER)

def motivo_do_projeto():

    _temp_stack = """ J'ai utilisé mes connaissences 
    en programmation pour créer un petit programme 
    sur la France. 
    
    C'est un moyen d'améliorer mes compétences de 
    programmeur tout en étudiant le français."""
    MOTIVO = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)
        
    for char in MOTIVO: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

    print(DIVIDER)
    