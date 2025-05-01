def div(a, b):
    print(a/b)


def specal_fucntion(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)

    return inner


div = specal_fucntion(div)
div(2, 4)
