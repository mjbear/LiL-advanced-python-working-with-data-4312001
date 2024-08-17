# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# TODO: use a dictionary to count each element
# fruitCounter = dict()
# fruitCounter = defaultdict(int)
fruitCounter = defaultdict(lambda: 100)

# TODO: Count the elements in the list
# this will fail with a normal dictionary because the key does not exist
for fruit in fruits:
    fruitCounter[fruit] += 1

# lots of unnecessary code while using a normal dictionary
# for fruit in fruits:
#     if fruit in fruitCounter.keys():
#         fruitCounter[fruit] += 1
#     else:
#         fruitCounter[fruit] = 1

# TODO: print the result
print(fruitCounter)
print()

for k, v in fruitCounter.items():
    print(f'{k}: {v}')
