import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    N, M, P, S = map(int, input[:4])
    
    aux = [0] * N
    index = 4
    for _ in range(M):
        u = int(input[index]) - 1
        v = int(input[index+1]) - 1
        aux[u] |= (1 << v)
        aux[v] |= (1 << u)
        index += 2

    pães = list(range(0, P))
    salsichas = list(range(P, P + S))
    extras = list(range(P + S, N))
    num_extras = len(extras)
    
    qnt_sets = []
    for mask in range(1 << num_extras):
        m_bits = 0
        validos = True
        for i in range(num_extras):
            if mask & (1 << i):
                atual_recheio = extras[i]
                m_bits |= (1 << atual_recheio)
                if aux[atual_recheio] & m_bits:
                    validos = False
                    break
        if validos:
            qnt_sets.append(m_bits)
            
    total = 0
    for p in pães:
        for s in salsichas:
            if not (aux[p] & (1 << s)):
                for subset_mask in qnt_sets:
                    if not (aux[p] & subset_mask) and not (aux[s] & subset_mask):
                        total += 1
    
    print(total)

if __name__ == "__main__":
    solve()