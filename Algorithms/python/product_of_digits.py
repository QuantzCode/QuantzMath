a = int(input("Give me a digit number "))
a = str(a)
product = 1
d = 0
b = 0
while b == 0:
    while d < len(a):
        product = product * int(a[d])
        d = d + 1
        print(product)

