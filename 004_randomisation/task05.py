# joining lists

# + operator
# less memory efficient as it creates new list
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

# using extend
# more memory efficient as it extends list in place
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# unpacking
# allows to merge more lists but slower
# can also add new items
c = [1, 2, 3]
d = [4, 5, 6]
combined = [*c, *d, 7]
print(combined)

# itertools.chain
# overkill for small data and usually good with big data
from itertools import chain
e = [1, 2, 3]
f = [4, 5, 6]
combined_chain = list(chain(e,f))
print(combined_chain)