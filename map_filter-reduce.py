#MAP
'''
def square(x):
    return x*x
l= [1,2,4,5,6,7]
newl = list(map(square,l))
print(newl)'''

'''def cube(x):
    return x*x
l= [1,2,4,5,6,7]
newl = list(map(cube,l))
print(newl)'''

#FILTER

l = [1,2,3,4,5,6,7]
def filter_function(a):
    return a>5

newnewl = list(filter(filter_function,l))
print(newnewl)

