
#initialize dictionary with defaul values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

disct1 = dict.fromkeys(employees, defaults)
print(disct1)

print(disct1["Kelly"])