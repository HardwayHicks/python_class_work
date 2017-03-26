t = "a", "b", "C"
print(t)

print("a", "b", "C")
print(("a", "b", "C"))

#  you can have different data types in a tuple
#  lists can only contain the same type of data (string, int, etc)

herp = "string 1", "string 2", 12, (
    ("new tuple 1", 1), ("new tuple 2", 2))

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
a, b, c, d = herp
print(a)
print(b)
print(c)
print(d)

f, g = d #  this pulls the tuples out of the tuple apparently

print("=" * 15)


print(f)
print(g)

print("=" * 15)


imelda = "more mayhem", "imelda may", 2011, (
    (1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "kentish town waltz"))

aa, bb, cc, dd = imelda

print(aa)
print(bb)
print(cc)
for i in dd:
    ff, gg = i
    print("\t", ff, gg)
#  alternately  it could be this
print("=" * 15)
for song in dd:
    track, title = song
    print("\tno.{}. Title: {}".format(track, title))













