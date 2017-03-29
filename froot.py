fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit that grows in bunches",
         "lime": "a sour, green, citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can i have some more fruit please"}

print(veg)

veg.update(fruit)
print(veg)

print(fruit.update(veg))  # this is going to throw null, the .update menthod doesn't create a new dictionary

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)

