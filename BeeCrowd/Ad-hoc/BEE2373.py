N = int(input())

quantidade = 0

for _ in range(N):
    L, C = map(int, input().split())
    
    if L>C:
        quantidade+=C
    
print(quantidade)