def product(a,b):
    if a < b:
        return product(b, a)
    elif b!=0:
        return a + product(a, b - 1)
    else:
        return 0
a = int(input("Give me a number? "))
b = int(input("Give me another number"))
print(product(a,b))