#python program iterating in dictionary

d = {1: 'name', 2: 'gender', 'age':22}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(f"{key}: {value}")