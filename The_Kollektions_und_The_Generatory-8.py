n = int(input())
A = [int(i) for i in input().split()]
m = int(input())
B = [int(i) for i in input().split()]
C = sorted(A + B)
print(' '.join(str(x) for x in C))