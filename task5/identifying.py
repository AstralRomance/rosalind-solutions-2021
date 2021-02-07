source_dict = {}
current_key = ''
with open('rosalind_gc.txt', 'r') as inp_f:
    file_string = inp_f.read()
    temp = ''
    for line in file_string.splitlines():
        if ('>' in line):
            print(line)
            source_dict[line] = temp
            temp = ''
            continue
        if '>' not in line:
            temp += line

source_dict.pop('', None)
#print(source_dict)

max_error = ()
current_max_error = 0
for source_item in source_dict.items():
    print(source_item)
    current_error = (sum([source_item[1].count('C'), source_item.count('G')])/len(source_item[1]))*100
    if current_error>=current_max_error:
        current_max_error = current_error
        max_error = (source_item[0], current_max_error) 

print(max_error)
print(''.join((max_error[0][1::], '\n', str(max_error[1]))))
