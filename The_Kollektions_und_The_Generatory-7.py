n = int(input())
Pk = [int(i) for i in input().split()]
m = int(input())
Qk = [int(i) for i in input().split()]
P = {}
Q = {}

k = n + 1
for i in range(n+1):
    P[k] = Pk[-(i+1)]
    k -= 1

l = m + 1
for j in range(m+1):
    Q[l] = Qk[-(j+1)]
    l -= 1

if len(Pk) >= len(Qk):
    R = P.copy()
    for key, value in Q.items():
        if key in R:
            R[key] += value
        else:
            R[key] = value
else:
    R = Q.copy()
    for key, value in P.items():
        if key in R:
            R[key] += value
        else:
            R[key] = value
Rk = []
for key, value in R.items():
    Rk.insert(0, value)
print(' '.join(str(x) for x in Rk))