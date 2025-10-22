def ultrapassagens(largada, chegada):
    posicao = {competidor: i for i, competidor in enumerate(largada)}

    nova_chegada = [posicao[competidor] for competidor in chegada]

    ultrapassar = 0
    N = len(nova_chegada)
    for i in range(N):
        for j in range(i+1, N):
            if nova_chegada[i]>nova_chegada[j]:
                ultrapassar+=1
    
    return ultrapassar

try:
    while True:
        N = int(input())
        largada = list(map(int, input().split()))
        chegada = list(map(int, input().split()))
        print(ultrapassagens(largada, chegada))
except EOFError:
    pass