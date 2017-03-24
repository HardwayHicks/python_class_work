# for i in range(10):
#     print("i is now a {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1


# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("choose a direction: ")
#     if chosen_exit == "quit":
#         print("game over man")
#         break
#
# else:
#     print("aren't you glad you got out of there")

import random

highest = 3
answer = random.randint(1, highest)

print("please guess a number between 1 and {}: ".format(highest))
guess = int(input())
while guess != answer:
    if guess == 0:
        break
    if guess != answer:
        if guess < answer:
            print("higher")
        else:  # to trigger the else the guess must be higher than the answer
            print("lower")
        guess = int(input())
        if guess == answer:
            print("well done amigo")
            break
else:
    print("you got it first try!")