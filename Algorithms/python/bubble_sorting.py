array = [12,35,46,75,29]
array[0] = int(input("What is the first number in the array? "))
array[1] = int(input("What is the second number in the array? "))
array[2] = int(input("What is the third number in the array? "))
array[3] = int(input("What is the fourth number in the array? "))
array[4] = int(input("What is the fifth number in the array? "))
print("This program shall arrange the array in ascending order")
print("Right now the array has been arranged in a random order with random numbers")
print("This is the array!")
print(array)
c = 0
for i in array: 
    if len(array) > 1:
        if array[0] > array[1]:
            c = array[0]
            array[0] = array[1]
            array[1] = c
        elif array[0] < array[1]:
            pass
        #next time
        if array[1] > array[2]:
            c = array[1]
            array[1] = array[2]
            array[2] = c
            pass
        elif array[1] < array[2]:
            pass
        #next time
        if array[2] > array[3]:
            c = array[2]
            array[2] = array[3]
            array[3] = c
        elif array[2] < array[3]:
            pass
        #next time
        if array[3] > array[4]:
            c = array[3]
            array[3] = array[4]
            array[4] = c
        elif array[3] < array[4]:
            pass
    print(array)