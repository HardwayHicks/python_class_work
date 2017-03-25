ipNumber = input("enter your ip: ")
digits = 0
placeCount = 0

for i in range(0, len(ipNumber)):
    if ipNumber[i] in '0123456789':
        digits += 1
    else:
        placeCount += 1
        print("there are {0} at the {1} mark".format(digits, placeCount))
        digits = 0
if i != '.':
    placeCount += 1
    print("there are {0} at the {1} mark".format(digits, placeCount))




