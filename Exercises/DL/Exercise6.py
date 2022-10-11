# deepcopy
from copy import deepcopy

person1 = ["sven", ['Street1', 'Brooklyn']]
person2 = person1.copy()
#person2 = deepcopy(person1)
person2[0] = 'Sarah'
print(person2)
person2[1][0] = 'street2'
print(id(person2))
print(id(person1))

