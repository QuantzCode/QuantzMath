a = int(input("Give me the lower number "))
b = int(input("Give me the upper number "))
def checkprime(a):
    c = 0
    for i in range(2, a):
        if a % i == 0:
            #print("Your number is composite")
            c = 1
            break
    if c == 0:
        print("{} is Prime".format(a))
e=[]
for i in range(a,b):
    if i % 2 != 0:
        e.append(i)
for x in e:
    checkprime(x)