a = [256, 37984, 473, 307]
minimum = a[0]
for i in range(0,len(a) - 1):
        if a[i] < minimum:
            minimum = a[i]
            pass
print(minimum)