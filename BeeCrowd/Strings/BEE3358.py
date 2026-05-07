N = int(input())

vogais = ['a', 'e', 'i', 'o', 'u']

for _ in range(N):
    contador_consoante = 0
    dificil = False

    sobrenome = input().strip().lower()

    for s in sobrenome:
        if s not in vogais:
            contador_consoante += 1
        else:
            contador_consoante = 0

        if contador_consoante >= 3:
            dificil = True
            break

    if dificil:
        print(f'{sobrenome.capitalize()} nao eh facil')
    else:
        print(f'{sobrenome.capitalize()} eh facil')