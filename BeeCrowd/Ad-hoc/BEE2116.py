def primo(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def maior_primo(l):
    for numero in range(l, 1, -1):
        if primo(numero):
            return numero
    return None

N, M = map(int, input().split())

p1 = maior_primo(N)
p2 = maior_primo(M)

print(p1*p2)

