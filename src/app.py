def ler_opcao_numerica():

    while True:
        try:
            return int(input('Escolha uma das opções: '))
        except ValueError:
            print('[ERRO]: Valor digitado inválido')
            continue