N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
x = [[None for i in range(N+1)] for j in range(M+1)]

def maxVal(i, C):
    if i == N:
        return 0
    else:
        skip = maxVal(i+1, C)
        if w[i] <= C:
            take = v[i] + maxVal(i+1, C-w[i])
        else:
            take = -1
        return max(skip, take)

print(maxVal(0, M))