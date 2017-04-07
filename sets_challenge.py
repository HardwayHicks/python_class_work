# set_menu_b = {"a", "e", "i", "o", "u"}
#
# inputtext = input("enter your random text here: ").lower()
# new_text = list(inputtext)
# # print(new_text)
# newset = set(new_text)
#
# blurb = sorted(newset.difference(set_menu_b))
#
#
# for letters in blurb:
#     print(letters)

new_text = set(input("enter your random text here:").lower())
vowels = frozenset("aeiou")
final_text = sorted(new_text.difference(vowels))
print(final_text)
for letters in final_text:
    print(letters)