def jose(n,k):

    pos = 0

    for i in range(1,n+1):

        pos = (pos + k) % i
        

    return pos + 1



N = int(input())

for i in range(N):

    n, k = map(int, input().split())

    print(f"Case {i + 1}: {jose(n,k)}")