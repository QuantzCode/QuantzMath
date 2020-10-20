a = int(input("Give me a number"))
c = 0
for i in range(2, a):
    if a % i == 0:
        print("Your number is composite")
        c = 1
        break
if c == 0:
    print("Your number is Prime")