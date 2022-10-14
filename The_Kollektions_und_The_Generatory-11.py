def funckcia_vsem_funckciam():
    funck = [i for i in input().split()]
    if funck[0] == 'push':
        push(funck[1])
    elif funck[0] == 'pop':
        pop()
    elif funck[0] == 'front':
        front()
    elif funck[0] == 'size':
        size()
    elif funck[0] == 'clear':
        clear()
    elif funck[0] == 'exit':
        exit()
    else:
        exit()

def push(chyslo):
    a.append(chyslo)
    print('ok')
    funckcia_vsem_funckciam()

def pop():
    if a != []:
        print(a.pop(0))
    else:
        print('error')
    funckcia_vsem_funckciam()

def front():
    if a != []:
        print(a[0])
    else:
        print('error')
    funckcia_vsem_funckciam()

def size():
    print(len(a))
    funckcia_vsem_funckciam()

def clear():
    a.clear()
    print('ok')
    funckcia_vsem_funckciam()

def exit():
    print('bye')

a = []
funckcia_vsem_funckciam()