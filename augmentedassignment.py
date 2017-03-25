number = "5,923,459,028,345,090"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]


newNumber = int(cleanedNumber)
print("the number is {}".format(newNumber))
