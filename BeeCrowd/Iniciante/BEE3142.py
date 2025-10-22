import sys

def calcula_coluna(valor):
    numero = 0
    for letra in valor:
        numero = numero * 26 + (ord(letra) - ord('A') + 1) #Transformando em número igual no cifra de césar
    return numero

for linha in sys.stdin:
    coluna = linha.strip()
    if not coluna:
        continue
    entrada = calcula_coluna(coluna)
    if entrada > 16384:
        print("Essa coluna nao existe Tobias!")
    else:
        print(entrada)
