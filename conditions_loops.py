p = True
q = False

if p and q:
    print('p and q =  TRUE')
else:
    print('p and q =  NOT TRUE')
    
if p or q:
    print('p or q =  TRUE')
else:
    print('p or q =  NOT TRUE')

# xor
if p ^ q:
    print('p xor q =  TRUE')
else:
    print('p xor q =  NOT TRUE')


for i in range(2, 10):
    if i==3:
        continue
        #pass
    print(i)
    if i==7:
        break


def sum(a, b):
    return a + b

print(sum(56, 645))

'''
This is a 
multi
line
comment

'''