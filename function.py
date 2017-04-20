def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep  # use SEP to add a space into things, it defaults to a space unless otherwise changed
    left_margin = (80 - len(text)) // 2

    return " " * left_margin, text
# parameter refers to the variables defined inside the function

# with open("centered", mode='w') as centered_file:

  # argument is the variables that are sent to the function
print(center_text("spam and eggs"))
print(center_text("spam, spam and eggs"))
print(center_text(12))
print(center_text("spam, spam, spam and spam"))
print(center_text("first", "second", 3, 4, "spam", sep=":"))