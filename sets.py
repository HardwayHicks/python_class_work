farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 25)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
#  this is a list turned into a set by using the set function
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

#  have to sue the SET constructor when creating an empty set, otherwise it creates a dictionary IE: empty_set2
empty_set = set()
empty_set2 = {}
empty_set.add("a")
# empty_set2.add("a")

even = set(range(0, 40, 2))
print(even)

squares_tuple = (4, 6, 8, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

print("=" * 25)

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))
#  union combines the two sets but does not create duplicate entries
print(even.union(squares))
print(len(even.union(squares)))


print("=" * 25)
#  intersection creates a set of only the entries that are shared using the '&' is the same as 'intersection'
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("=" * 25)

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

#  the 'difference' method is only applicable for SETS
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

print("=" * 25)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))
print("=" * 25)

# symmetric difference is everything that belongs to all SETs
print("symmetric even minus the squares")
print(sorted(even.symmetric_difference(squares)))
print("symmetric squares minus the evens")
print(sorted(squares.symmetric_difference(even)))
print("=" * 25)

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
if 8 in squares:
    squares.remove(8)

print("=" * 25)

even = set(range(0, 40, 2))

squares_tuple2 = (4, 6, 16)
squares2 = set(squares_tuple2)
print(squares2)

if(squares2.issubset(even)):
    print("squares is a subset of even")

if even.issuperset(squares2):
    print("even is a super set of squares")

print("=" * 25)
# a frozenset is imutable and can be used as a dictionary key










