a = int(input("Give me a number "))
a = str(a)
d = 0
sum = 0
while d < len(a):
    sum = sum + int(a[d])
    d = d + 1
print(sum)
