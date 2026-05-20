while True:
    N = int(input())

    if N == 0:
        break

    problemas_corretos = set()
    penalidades = {}

    contador_corretos = 0
    soma_tempo = 0

    for _ in range(N):
        identificador, tempo, julgamento = input().split()
        tempo = int(tempo)

        if identificador not in penalidades:
            penalidades[identificador] = 0

        if julgamento == "incorrect":
            penalidades[identificador] += 1

        elif julgamento == "correct":
            if identificador not in problemas_corretos:
                contador_corretos += 1

                soma_tempo += tempo + (20 * penalidades[identificador])

                problemas_corretos.add(identificador)

    print(contador_corretos, soma_tempo)