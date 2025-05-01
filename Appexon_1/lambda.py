def list_1(fun,element):
    c =[]
    for i in element:
        values = fun(i)
        c.append(values)
    print(c)

a = lambda x : x ** 3
element = [1,2,3,4]
list_1(a,element)