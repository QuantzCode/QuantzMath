a = [45, 46, 48, 49, 100, 3994]
b = int(input("Give me a number in the array "))
c = 0
for i in range(0, len(a)):
    if a[i] == b:
        print(i)
        c = 1
if c == 0:
    print("Your number is not in the list ")