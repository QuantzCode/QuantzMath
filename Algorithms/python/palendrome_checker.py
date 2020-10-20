d = 0
while d == 0:
    a = str(input("Give me a word ? "))
    pizza  = (a)
    if pizza[::-1] == pizza[::1]:
        print("Your word is a palendrome")
    else:
        print("You are not a palendrome, stop wasting my time! ")