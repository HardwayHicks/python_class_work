t = "a", "b", "C"
print(t)

print("a", "b", "C")
print(("a", "b", "C"))

#  you can have different data types in a tuple
#  lists can only contain the same type of data (string, int, etc)

herp = "string 1", "string 2", 123

print(herp)
print("=" * 14)
print(herp[0])
print("=" * 14)
print(herp[1])
print("=" * 14)
print(herp[2])

#  [] after a tuple is the index number

#  tuple looks like this - variable = contents1, contents 2
#  list looks like this - variable = [contents1, contents 2]
print("=" * 15)

# unpacking the tuple
a, b, c = herp
print(a)
print(b)
print(c)
