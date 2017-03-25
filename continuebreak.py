# shopping_list = ["milk", "pasta", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy " + item)

meal =["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("i'll have a plate of that then")
if nasty_food_item:
    print("can't i have anything without spam in it?")