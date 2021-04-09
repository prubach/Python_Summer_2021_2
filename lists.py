li = [ 235245, 23534263, 2342, 78678, 2342, 3, 354]


for elem in li:
    #print(elem)

    print('Element: %i at position: %s' % (elem, li.index(elem)))
    #print(li.index(elem))

li.sort()
print()
for i in range(len(li)):
    print('Element: %i at position: %s' % (li[i], i))

li2 = [ 235245.6363, ' abbavcaf', 'srtr', 23534263, 2342, 78678, 2342, 3, 354]

print()

for elem in li2:
    print('Element: %s at position: %s' % (elem, li2.index(elem)))

print()
li2.append('afsfgs')
print(li2)
li2.insert(3, 'afsfgs')
print(li2)

print(li2[3:])

print(li2[-2:])
print(li2[:-5])

print(li2[:-5])

#li2.sort()
# Redirect output stream and error stream on Unix
# python lists.py > out 2>out_err
#print(li)