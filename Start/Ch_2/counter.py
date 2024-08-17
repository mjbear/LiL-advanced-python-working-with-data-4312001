# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# TODO: How many students in class 1 named James?
print(c1['James'])

# TODO: How many students are in class 1?
print(sum(c1.values()), 'students in class 1')

# TODO: Combine the two classes
c1.update(class2)
print(sum(c1.values()), 'students in class 1 (after combining)')

# can also combine a Counter object too
# c1.update(c2)
# print(sum(c1.values()), 'students in class 1 (after combining again)')

# TODO: What's the most common name in the two classes?
print(c1.most_common(3))

# TODO: Separate the classes again
c1.subtract(class2)
print(c1.most_common(1))

# TODO: What's common between the two classes?
# intersection
print('\nIntersection:')
print(c1 & c2)

# union
print('\nUnion:')
print(c1 | c2)

# difference
print('\nDifference from c1 to c2:')
print(c1 - c2)
print('\nDifference from c2 to c1:')
print(c2 - c1)