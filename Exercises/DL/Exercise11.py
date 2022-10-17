
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
dict1 = {key:value for ( key, value) in sampleDict.items()}
dict2 = {k*2:v for (k,v) in sampleDict.items() if k == 'History'}
print(dict1)
print(dict2)

D = {}
for x in range(5):
    D[x] = x**2

print(D)
# Prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

