string = "1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

an_list = ["herp", "sherp", "derp", "blerp"]
an_iter = iter(an_list)
n = len(an_list)

for n in an_list:
    print(next(an_iter))
