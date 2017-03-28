# my_list = ["a", "b", "c", "d"]
#
# new_string = ''
#
# new_string = ", ".join(my_list)
#
# print(new_string)
#
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# newer_string = ''
# newer_string = ", ".join(letters)
#
# print(newer_string)

locations = {0: "you are sitting in front a computer learning Python",
             1: "you are standing at the end of a road before a small brink building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in the forest"}
#
exits = {0: {"q": 0},
         1: {"w": 2, "e": 3, "n": 5, "s": 4, "q": 0},
         2: {"n": 5, "q": 0},
         3: {"w": 1, "q": 0},
         4: {"n": 1, "w": 2, "q": 0},
         5: {"w": 2, "s": 1, "q": 0}}

# exits = {0: {"q"},
#          1: {"w": 2, "e": 3, "n": 5, "s": 4}
#          }

vocabulary = {"quit": "q",
              "north": "n",
              "south": "s",
              "east": "e",
              "west": "w"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))








loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys()) + ": "

    # available_exits = ""
    # for direction in exits[loc].keys():
    #     available_exits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("available exits are " + available_exits + " ").lower()
    print()
    # parse user input here if needed
    if len(direction) > 1: #more than one letter
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]

        # for word in vocabulary: # this is checking for input in the vocabulary dictionary where WORD becomes the actual key
        #     if word in direction: # this checks if the key is accessable by making sure the key is contained in the available directions (n,s,e,w
        #         direction = vocabulary[word] #  this sets the KEY to the direction variable, replacing the original input
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go that way")


# keywords = {"n": "north" "norte" "go north"}
#
# print(keywords["n"])