import sys, time
DIVIDER = '=' * 60

def titulo():

    _temp_stack = """========== 🇫🇷 LA FRANCE 🇫🇷 =========="""
    BANNER = "\n".join(l.center(57) for l in _temp_stack.splitlines())

    print(DIVIDER)
        
    for char in BANNER: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()
