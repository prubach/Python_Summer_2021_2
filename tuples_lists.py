li1 = [1, 0, 4654, 4]
li2 = [3, 6, 4, 21]
li3 = [li1, li2]
print(li3)
print(li3[0][2])

t1 = (14, 15)
t2 = (24, 243, 54)
print(t2[1])

a, b, c = t2
print(a)
print(b)
print(c)

print()
d1 = {'a': 10, 'b': 11, 'c': 12}
#d1 = {'a': 10, 'b': 11, 'c': 12, 'a': 43}

print(d1['a'])

print(list(d1.values()))

print(list(d1.keys()))

for key in d1.keys():
    print(d1[key])
