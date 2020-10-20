array = []
d = 0
a = int(input("How many numbers would you like to check for? "))
for i in range(0,a):
    b = int(input("Enter the number? "))
    array.append(b)
while d < a:
    for j in range(0,len(array) - 1):
        if array[j] < array[j + 1]:
            c = array[j]
            array[j] = array[j + 1]
            array[j + 1] = c
    d = d + 1
print(array)
