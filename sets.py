'''set = {1,23,4,5,3,2,2}
print(set)
print(type(set))

my_list = {1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3}
print(my_list)

# BOOLEANS

b = type(False)
print(b)

c = 1==1
print(c)

v = 8>10
print(v)'''

set1= {1,2,"a",4,5}
print(set1)

set2 = set([1,2,4,3,5])   #it converted list to set.
print(set2)

set2.add(8)
print(set2)

set2.update([9,10])
print(set2)

set2.discard(5)
print(set2)

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = {5,6,7,8,9}
print(set5)
print(len(set5))

print(set4.isdisjoint(set5))
print(set4.issubset(set5))