# jabber = open("C:\\Users\\Isz\\Downloads\\FileIO\\sample.txt", 'r')
# don't need to use the path if the file exists in the same directory as the project

# jabber = open("sample.txt", 'r')
#
# # must use the double \\ on windows, linux and macos need a /
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
# # using end='' prevents the print from adding another line for each carrige return
#
#
# jabber.close()

# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB"in line.upper():
#             print(line, end= '')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()


# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')