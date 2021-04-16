l1 = [[3, 6, 9], [6, 8, 5], [9, 7, 2]]
# sum rows
# sum cols
# sum of all elements
row_sum = [0, 0, 0]
col_sum = [0, 0, 0]

#rows
sum_r=[sum(i) for i in l1]
print(sum_r)

sum_col = [sum([row[i] for row in l1]) for i in range(0,len(l1[0]))]
print(sum_col)

sum_all=sum([sum(i) for i in l1])
print(sum_all)

import numpy as np

print(np.sum(l1, axis=1))
print(np.sum(l1, axis=0))
print(np.sum(l1))
