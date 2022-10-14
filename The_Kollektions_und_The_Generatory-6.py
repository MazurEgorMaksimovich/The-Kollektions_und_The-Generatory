n = int(input())
aa = ['*']*n
for i in range(n):
    a = [j for j in input().split()]
    a.insert(0, str(round(float((int(a[1]) + int(a[2]) + int(a[3]))/3), 2)))
    a[0] = -(float(a[0]))
    aa[i] = a
aa.sort()

for i in range(n):
    a = aa[i]
    a.append(a.pop(0))
    j = str(abs(a[4]))
    if j[-2:-1] == '.':
        a[4] = j + '0'
    else:
        a[4] = j
    print(' '.join(str(x) for x in a))