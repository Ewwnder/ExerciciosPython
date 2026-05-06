N = int(input())

menor_valor = float('inf')

for _ in range(N):
    P, G = input().split()
    P = float(P)
    G = int(G)

    preco_Kg = P*1000/G

    if preco_Kg<menor_valor:
        menor_valor = preco_Kg

print(f'{menor_valor:.2f}')