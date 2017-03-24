for i in range(1,29):
    print("i is now {}".format(i))

number = "9,223,323,425,523,524,854"
for i in range(0, len(number)):
    print(number[i])

print("*******************")

number = "9,223,323,425,523,524,854"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("the number is {}".format(newNumber))