def odd_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(odd_even(19))
def prime(x):
    c = 0
    for i in range(2,x):
        if x % i == 0:
            return False
            c = c + 1
            break
    if c == 0:
        return "Yes it is a Prime"
print(prime(7))