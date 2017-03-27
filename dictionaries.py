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
while True:
    dict_key = input("please enter an fruit: ")
    if dict_key == "quit":
        break
    desc = fruit.get(dict_key, "we don't have a " + dict_key)
    print(desc)
    # if dict_key in fruit:
    #     desc = fruit.get(dict_key)
    #     print(desc)
    # else:
    #     print("not valid froot")
