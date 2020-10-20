def check_prime(a):
    isdivisible = False
    for i in range(2,a):
        if a % i == 0:
            isdivisible = True
    if isdivisible == False:
        return 1
def check_twin_prime(a, b):
    if check_prime(a) and check_prime(b):
        print("{} and {} are twin primes".format(a, b))

e = []
for i in range(2,1001):
    if i % 2 != 0:
        e.append(i)
for x in range(0, len(e)- 1):
    check_twin_prime(e[x], e[x + 1])