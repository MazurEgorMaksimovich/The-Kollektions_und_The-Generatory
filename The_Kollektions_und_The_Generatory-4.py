n = int(input())
aa = ['*']*n
for i in range(n):
    a = [j for j in input().split()]
    a[1::] = [str(round(float((int(a[1]) + int(a[2]) + int(a[3]))/3), 2))]
    j = a[1]
    if j[-2:-1] == '.':
        a[1] = j + '0'
    aa[i] = a

for i in range(n):
    a = aa[i]
    print(' '.join(str(x) for x in a))