a = int(input("Give me a number "))
sum = 0
for d in range(1,a):
    if a % d == 0:
        sum = sum + d
if sum == a:
    print("Your number is a perfect number")
else:
    print("Your number is not a perfect number")