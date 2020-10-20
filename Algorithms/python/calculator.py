#hello
#lets get started
print("Hello User, what can we call you? ")
username = str(input("What is your username? "))
print("Not a bad name " + username) #it works as username is already a string
while True: #forever loop
    print("1) Basic Operations")
    print("2) One number Operations")
    a = int(input("Choose which one? "))
    if a == 1:
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        a = int(input("Choose which one? "))
        if a == 1:
            iter = int(input("How many numbers do you want to add? "))
            b = 0
            while iter > 0:
                i = int(input("Give me your number? "))
                b += i
                iter -= 1
            print("The sum of all the arguments you provided is " + str(b))
        elif a == 2:
            a = int(input("Give me the Minuend? "))
            b = int(input("Give me the subtrahend? "))
            print("The answer is " + str(a - b))
        elif a == 3:
            iter = int(input("How many numbers do you want to multiply? "))
            b = 1
            while iter > 0:
                i = int(input("Give me your number? "))
                b *= i
                iter -= 1
            print("The product of all the arguments you provided is " + str(b))
        elif a == 4:
            a = int(input("Give me the number? "))
            b = int(input("Give me the number? "))
            print("The answer is " + str(a / b))
        else:
            print("Invalid option")
    elif a == 2:
        print("1) Square")
        print("2) Squareroot")
        print("3) Cube")
        print("4) Factorial")
        a = int(input("Choose? "))
        if a == 1:
            a = int(input("Give me your number? "))
            print("The answer is " + str(a * a))
        elif a == 2:
            a = int(input("Give me your number? "))
            for i in range(1, a):
                if i * i == a:
                    print("The squareroot of " + str(a), + " is " + str(i))
        elif a == 3:
            a = int(input("Give me your number? "))
            print("The answer is " + str(a * a * a))
        elif a == 4:
            b = 1
            a = int(input("Give me a number? "))
            for i in range(1, a + 1):
                c *= i
            print(c)
#done!!!
