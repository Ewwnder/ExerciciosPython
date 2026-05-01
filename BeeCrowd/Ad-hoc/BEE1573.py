import math

while True:
    A, B, C = map(int, input().split())

    if A==0 and B==0 and C==0:
        break

    volume_p = A*B*C
    arestas = int(volume_p**(1/3))


    #Só tem que fazer isso pq python de vez em quando calcula errado, mas em TEORIA não é necessário não.
    while (arestas+1)**3<=volume_p:
        arestas+=1
    while arestas**3>volume_p:
        arestas-=1
    
    print(arestas)