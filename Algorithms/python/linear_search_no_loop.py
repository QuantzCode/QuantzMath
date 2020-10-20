a = [45, 46, 48, 49, 100, 3994]
b = int(input("Give me a number in the array "))
if a[1] == b:
    print(str(a[1]) + " is in the array")
elif a[2] == b:
    print(str(a[2]) + " is in the array")
elif a[3] == b:
    print(str(a[3]) + " is in the array")
elif a[4] == b:
    print(str(a[4]) + " is in the array")
elif a[0] == b:
    print(str(a[0]) + " is in the array")
else:
    print("Your number is not in the array")