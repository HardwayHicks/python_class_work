# parrot_list = ["not pinin'", "no more", "a stiff", "bereft of life"]
# parrot_list.append("an ex-parrot")
#
# for state in parrot_list:
#     print("this parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# number = even + odd
# # number.sort()
# # print(number)
# numbers_in_order = sorted(number)
#
# print(numbers_in_order)

# list_1 = []
# list_2 = list()
#
# print("list 1: {}".format(list_1))
# print("list 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("the lists are equal")

#
# another_even = list(even)
#
# print(another_even == even)
#
# another_even.sort(reverse=True)
# print(even)
# print(another_even)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
# print(numbers)
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)


menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for food in meal:
            print(food)



















