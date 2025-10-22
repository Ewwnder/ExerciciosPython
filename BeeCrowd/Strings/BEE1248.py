N = int(input())

for _ in range(N):
    dieta = input().strip()
    cafe_manha = input().strip()
    almoco = input().strip()

    comeu = cafe_manha+almoco

    cheater = False

    dieta_lista = list(dieta)

    for comida in comeu:
        if comida in dieta_lista:
            dieta_lista.remove(comida)
        else:
            cheater = True
            break
    
    if cheater:
        print("CHEATER")
    else:
        janta = sorted(dieta_lista)
        print(''.join(janta))