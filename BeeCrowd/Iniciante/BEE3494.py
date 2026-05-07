S = input().strip()
T = input().strip()

custo_arrumar = 0

for a, b in zip(S, T): #O zip é para comparar, no caso vai ficar: 'a' - 'a' | 'z' - 'a' | 'u' - 'l' | 'r' - 'a' -> Importante levar para maratonas, acho que ajuda nos de comparação
    diferenca = abs(ord(a)-ord(b))
    custo_arrumar+=min(diferenca, 26-diferenca)

print(custo_arrumar)