import json
import os
# current working directory
print(os.getcwd())
#out_file = os.path.join('data', 'out_list.json')
out_file = os.path.join(os.getcwd() + '/data', '..', 'out_list.json')

if os.path.exists(out_file):
    print(out_file + ' exists!')
else:
    print(out_file + ' does not exist!')
    exit(10)

with open(out_file, 'r') as f:
    out_obj = json.load(f)
    print(out_obj)
    print(sum(out_obj[0]))

# list files in the project folder
#print(os.listdir(os.getcwd()))
for f in os.listdir(os.getcwd()):
    print(f + ' ' + str(os.path.isfile(f)))
    print(f + ' ' + str(os.path.isdir(f)))