# DICTIONARIES :-- IT IS UNORDERED MAPPING FOR STORING OBJECTS.
# Where to use dictionary and list. :---> DICTIONARY : Object retrieved ny key name. LIST : Object retrieved by location.

'''dict = {'name':"sunny", 'age':19}
print(dict)
print(type(dict))

prices_lookup = {"apples" : 23, "oranges": 52, "pineapple" : 89}
print(prices_lookup)
print(prices_lookup["apples"])
print(prices_lookup["pineapple"])

my_dict = {'k1':'apples','k2' : [1,234,45],'k3' : {"inside dict":'dictionary'}}
print(my_dict)
print(my_dict['k2'])
print(my_dict['k2'][2])

d = {"k1":100, "k2":200, "k3":300}
print(d)
print(d["k1"])
d["k1"] = 'NEW VALUE'
print(d)

d = {"k1":100, "k2":200, "k3":300}
d1 = d.keys()
print(d1)

d2 = d.values()
print(d2)

print(my_dict['k1'].upper())'''

# SUBTRACTION IN THE DICTIONARY

'''d["k1"] = d["k1"] - d["k2"]
print(d["k1"])

dict_yo = {'first':700,'second':655,'third':200}

dict_yo['first'] += dict_yo['second']
print(dict_yo)

dict_yo['second'] -= dict_yo['third']
print(dict_yo)

dict_yo['third'] *= 2
print(dict_yo)

dict_yo['first'] = dict_yo['first']**2
print(dict_yo)'''

#We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:

dict = {}
dict['animal'] = 'dog'
dict['answer'] = 45
print(dict)
print(dict.items())

# NESTING OF A LIST.

d = {'key1':{'name':{'age':19}}}
print(d)
print(d.keys())
print(d.values())
