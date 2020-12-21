def root2(n):
    root = n**(1/2)
    return root

def root3(n):
    if n >= 0:
        cbrt = n**(1/3)
    else:
        cbrt = -((-n)**(1/3))
    return cbrt