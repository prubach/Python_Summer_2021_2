my_file = 'out'
i = 0
with open(my_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        i += 1
        print("%i: %s" % (i, line))
