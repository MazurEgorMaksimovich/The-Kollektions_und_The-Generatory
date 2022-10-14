def ser_arymf(a, n):
    k = 0
    for i in a:
        k += i
    ser_arymf_perem = str(round(float(k / n), 2))
    if ser_arymf_perem[-2:-1] == '.':
        ser_arymf_perem = ser_arymf_perem + '0'
    return ser_arymf_perem



n = int(input())
aa = [0]*3
math_a = []
phys_a = []
info_a = []

for i in range(n):
    a = [j for j in input().split()]
    math_a.append(int(a[1]))
    phys_a.append(int(a[2]))
    info_a.append(int(a[3]))

aa[0] = ser_arymf(math_a, n)
aa[1] = ser_arymf(phys_a, n)
aa[2] = ser_arymf(info_a, n)

print(' '.join(str(x) for x in aa), end=' ')