import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maint"] = {"stuck": ["oil"],
                  "loose": ["gaffe1r tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled_eggs"])

print(books["maint"]["loose"])
books.close()
