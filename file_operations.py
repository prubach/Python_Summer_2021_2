out_file = 'out.txt'
with open(out_file, 'a') as f:
    f.write('abc\n')
    f.write('def')
    f.write('feg')


l1 = [[3, 6, 9], [6, 8, 5], [9, 7, 2]]
out_file = 'out_list.txt'
with open(out_file, 'w') as f:
    f.write(str(l1))

print('------ PICKLE -------')
import _pickle
out_file = 'out_list.dat'
with open(out_file, 'wb') as f:
    _pickle.dump(l1, f)


with open(out_file, 'rb') as f:
    out_obj = _pickle.load(f)
    print(out_obj)
    print(sum(out_obj[0]))

print('------ JSON -------')
import json
out_file = 'out_list.json'
with open(out_file, 'w') as f:
    json.dump(l1, f)


with open(out_file, 'r') as f:
    out_obj = json.load(f)
    print(out_obj)
    print(sum(out_obj[0]))
