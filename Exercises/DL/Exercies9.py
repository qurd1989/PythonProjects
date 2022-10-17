
# convert list to into dictionary
keys = ['ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = dict(zip(keys, values))
print(res)
res1 = dict(map(lambda i,j : (i,j), keys,values))
print(res1)

# merging Dictionaries
dict_1 = {'John': 15, 'Rick1': 10, 'Misa' : 12 }
dict_2 = {'Bonnie': 18,'Rick': 20,'Matt' : 16 }

dict_3 = dict_1 | dict_2
print(dict_3)

dict_4 = dict_2.update(dict_1)
print(dict_4)

dict_5 = dict(dict_1, **dict_2)
print(dict_5)