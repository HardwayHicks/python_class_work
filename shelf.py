import shelve

# with shelve.open('ShelfTest') as fruit:
# the above opening opens the shelve and then closes its, the below method requires it to be manually
# closed via .close()
fruit = shelve.open('ShelfTest')

# shelf keys must be a string unlike a dictionary

# fruit['orange'] = "a sweet, orange fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit"
# fruit['lime'] = "a sour, green citrus fruit"
# this is a dictionary it can also be created by using key value pairs as below, that will in turn create an
# dictionary inside the shelve file
# can't create a shelve by using literals as below without it creating its own dictionary, don't do this its extra
# overhead


# print(fruit["lemon"])
# print(fruit["grape"])
#
# this will update the key's value, just like a dictionary
# fruit["lime"] = "great with tequila"s
#
# for snack in fruit:
#     print(snack + ' - ' + fruit[snack])

# while True:
#     dict_key = input("please enter an fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("we don't have an " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())


fruit.close()

print(fruit)

# with shelve.open('ShelfTest') as fruit:
#     fruit = {"orange": "a sweet, orange, citrus fruit",
#              "apple": "good for making cider",
#              "lemon": "a sour, yellow, citrus fruit",
#              "grape": "a small, sweet, fruit growing in bunches",
#              "lime": "a sour, green, citrus fruit"}
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# print(fruit)
