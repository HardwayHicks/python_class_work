fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green, citrus fruit"}

print(fruit)
#  can't use the index in a dictionary, it looks like a list but its got {},
#  but you can access the 'key' which is the thing at the beginning followed by the :

print(fruit["lemon"])

bike = {"make": "honda", "model": "250 dream", "color": "red", "engine_size": 250}

print(bike["engine_size"])
print(bike["color"])

#  this ads a new 'value' to a dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit)
print(fruit["pear"])

fruit["lime"] = "great with tequila"
print(fruit["lime"])
#  the last time a value is assigned is the value that is saved

#  deletes a value
del fruit["lemon"]
print(fruit)

#  creates empty dictionary
# fruit.clear()
# print(fruit)
print("="*15)

# print(fruit["tomato"])


#  this section prevents errors when entering a key that doesn't exist
# while True:
#     dict_key = input("please enter an fruit: ")
#     if dict_key == "quit":
#         break
#     desc = fruit.get(dict_key, "we don't have a " + dict_key)
#     print(desc)
    # if dict_key in fruit:
    #     desc = fruit.get(dict_key)
    #     print(desc)
    # else:
    #     print("not valid froot")
#
# for snack in fruit:
#     print(fruit[snack])

#  items in the dictionary aren't in a set order, you must use the key to get specific things.  It has to do with hashes and checksums


#  this is used to demostrate that the dictionary bascially has a specific order each time its created, so it will not have a
#  different order if called multiple times

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("=" * 20)

#  this creates a list from a dictionary
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#  a better way to write this:
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#  an even better way to write it would be:
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# using the .values you'll get the values of the dictionary as opposed to the keys as demonstrated with .keys
for val in fruit.values():
    print(val)
#  but its far more efficient to do it this way
print("=" * 20)

for key in fruit:
    print(fruit[key])
print("=" * 20)
print("=" * 20)

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)
print("=" * 20)
print("=" * 20)

#  use this to create tuples from dictionary keys and values
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)
print("=" * 20)

for snack in f_tuple:
    item, desc = snack
    print(item + " is " + desc)
print("=" * 20)
# can create dictionary from tuple and back
print(dict(f_tuple))














