n = int(input())
a = [int(i) for i in input().split()]
p = int(input())
print(' '.join(str(x) for x in a if x != p))