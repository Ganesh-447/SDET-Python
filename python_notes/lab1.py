

#function with both return type and argument.
def add(a,b):
    p = a+b
    return p

a = add(1,2)
print(a)
#function with  return type and no argument.
def add():
    a= 4
    b =5
    p = a+b
    return p

a = add()
print(a)

#function with  no return type and argument.
def add(a,b):
    p = a+b
    print (p)

v = add(10,2)

#function with  no return type and no argument.
def add():
    a =5
    b =6
    p = a+b
    print (p)

v = add()
