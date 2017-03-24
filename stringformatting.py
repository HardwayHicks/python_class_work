age = 25
print("my age is " + str(age) + " years")
print("my age is {0} years".format(age))

print("there are  {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(31, "jan", "mar", "may", "july", "august", "oct", "dec"))

print("""Jan:{2}
Feb: {0}
march: {2}
april: {1}""".format(29, 30, 31))

print("my age is %d years" % age)
print("my age is %d %s %d %s" % (age, "years", 6, "months"))

for i in range(1,12):
    print("no. %2d squared is %4d and cubed is %4d" %(i, i**2, i**3))


print("pi is approximately %12.50f" %(22/7))




for i in range(1,12):
    print("no. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))
