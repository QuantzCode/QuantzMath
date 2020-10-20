d = 2
st = 1
backwards = False
while st < 6:
    if backwards == False:
        print(" " * d + "*" * st + " " * d)
        d -= 1
        st += 2
    if st == 5:
        backwards = True
    if backwards == True:
        print(" " * d + "*" * st + " " * d)
        d += 1
        st -= 2
        if st == 1:
            break
print(" " * 2 + "*" + " " * 2)