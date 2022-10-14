n = int(input())
a = [int(i) for i in input().split()]
p = int(input())
a.pop(p-1)
q, k = (int(i) for i in input().split())
a.insert(q-1, k)
print(' '.join(str(x) for x in a))