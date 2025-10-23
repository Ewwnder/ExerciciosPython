T = int(input())

for _ in range(T):
    N = int(input())
    nome = input().split()
    registro = input().split()

    reprova = []

    for i in range(N):
        r = registro[i]
        p = r.count('P')
        f = r.count('A')

        total = p+f

        if total==0:
            freq = 1.0
        else:
            freq = p/total
        
        if freq<0.75:
            reprova.append(nome[i])
    
    print(' '.join(reprova))