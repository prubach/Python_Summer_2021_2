import os.path


def sum_bowls(r):
    if r==1:
        return 1
    else:
        return r + sum_bowls(r-1)

def sum_bowls_loop(r):
    sum = 0
    for i in range(1, r+1):
        sum=sum+i
    return sum


r = 5
#print(sum_bowls_loop(r))
print(sum_bowls(r))

#os.path.getsize()

# print(sum_bowls(4))
# print(sum_bowls(5))
#
# print(sum_bowls_loop(4))
# print(sum_bowls_loop(5))