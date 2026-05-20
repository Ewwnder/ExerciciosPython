import sys

entrada = sys.stdin.read().split()

if not entrada:
    exit()

N = int(entrada[0])
idx = 1

pilhas = []
for _ in range(N):
    K = int(entrada[idx])
    idx += 1
    pilha = []

    for _ in range(K):
        pilha.append(int(entrada[idx]))
        idx += 1
    pilhas.append(pilha)

if N >= 3 or N == 1:
    print('S')
elif N == 2:
    s1 = pilhas[0]
    s2 = pilhas[1]

    invariante = s1 + s2[::-1]
    
    if invariante == sorted(invariante):
        print('S')
    else:
        print('N')