import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["color"] = "red"
    # bike["engine_size"] = 250

    # this will remove a key from the shelve but will throw an error if executed twice
    # del bike['engin_size']

    for key in bike:
        print(key)

    print('*' *40)

    print(bike["engine_size"])
    print(bike["color"])
    # print(bike["engin_size"])


