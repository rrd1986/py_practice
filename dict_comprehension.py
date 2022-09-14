k = ["name", "age", "id"]
v = ["rashmi", "35", "XXXX1234"]

# dict comprehension

new_dict = { i: j for (i,j) in zip(k,v)}

print(new_dict)

# dict comprehension from list

x = {i : i**2 for i in [1, 2, 3,4]}
print(x)

y = {i : i**2 for i in [1, 2, 3,4] if i**2 % 2 == 0}

print(y)