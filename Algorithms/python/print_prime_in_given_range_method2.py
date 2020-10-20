a = int(input("Give me the lower number "))
b = int(input("Give me the upper number "))
while a < b:
    c = 0
    i = 2
    while i < a:
        if a % i == 0:
            c = 1
            break
        i = i + 1
    if c == 0:
        print("{} is a prime number".format(a))
    a = a + 1


