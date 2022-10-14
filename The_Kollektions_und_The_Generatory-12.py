def funckcia_vsem_funckciam():
    funck = [i for i in input().split()]
    if funck[0] == 'back_push' or funck[0] == 'push_back':
        back_push(funck[1])
    elif funck[0] == 'front_push' or funck[0] == 'push_front':
        front_push(funck[1])
    elif funck[0] == 'pop_front':
        pop_front()
    elif funck[0] == 'pop_back':
        pop_back()
    elif funck[0] == 'back':
        back()
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

def back_push(chyslo):
    a.append(chyslo)
    print('ok')
    funckcia_vsem_funckciam()

def front_push(chyslo):
    a.insert(0, chyslo)
    print('ok')
    funckcia_vsem_funckciam()

def pop_front():
    if a != []:
        print(a.pop(0))
    else:
        print('error')
    funckcia_vsem_funckciam()

def pop_back():
    if a != []:
        print(a.pop())
    else:
        print('error')
    funckcia_vsem_funckciam()

def front():
    if a != []:
        print(a[0])
    else:
        print('error')
    funckcia_vsem_funckciam()

def back():
    if a != []:
        print(a[-1])
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