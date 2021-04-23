
folder = 'documents'

# Use recursion...
def sum_space(folder):
    sum = 0
    #TODO ....
    return sum


import os

def sum_space_loop(folder):
    sum_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                sum_size += os.path.getsize(file_path)
    return sum_size
my_folder = "../Python_Summer_2021_2/data"
print("Total size is:" + str(sum_space_loop(my_folder)) + "byte")