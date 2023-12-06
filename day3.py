with open('inputs\day3_input.txt') as f:
    text = f.read()
text = '''000..000..
...*......
..00..000.
......#...
000*......
.....+.00.
..000.....
......000.
....$.....
.100.100..
'''
def get_digits(word,index):
    start = index
    end = index
    if not word[index].isnumeric():
        return ''
    while True:
        if word[start-1].isnumeric():
            start = start - 1
        elif end<len(word)-1 and word[end+1].isnumeric():
            end = end+1
        else:
            break
    return word[start:end+1]
def get_indexs(current_index):
    if current_index == 0:
        return [current_index,current_index+1]
    else:
        return [current_index-1,current_index,current_index+1]
data = dict(zip(range(len(text.split('\n'))),text.split('\n')))
new_data = {x:[] for x in range(len(text.split('\n')))}
#print(get_digits('467..114..',5))
#print(get_digits('467..114..',6))
#print(data)
other_dict = {}
for key in data:
    for index in range(len(data[key])):
        char = data[key][index]
        if char in "!@#$%^&*()\{\}[]=+:;<>,`~\\?/|_-'\"":
            checklist = get_indexs(index)
            for check in checklist:
                if key>0:
                    above = get_digits(data[key-1],check)
                    if above!='':
                        new_data[key-1].append(int(above))
                        if int(above) in other_dict:
                            other_dict[int(above)].append((key-1,check))
                        else:
                            other_dict[int(above)]=[(key-1,check)]
                if key!=len(data)-1:
                    below = get_digits(data[key+1],check)
                    if below!='':
                        new_data[key+1].append(int(below))
                        if int(below) in other_dict:
                            other_dict[int(below)].append((key+1,check))
                        else:
                            other_dict[int(below)]=[(key+1,check)]
                if check != index:
                    same_row = get_digits(data[key],check)
                    if same_row!='':
                        new_data[key].append(int(same_row))
                        if int(same_row) in other_dict:
                            other_dict[int(same_row)].append((key,check))
                        else:
                            other_dict[int(same_row)]=[(key,check)]
final_data = {key:set(value) for key,value in new_data.items()}

total = 0
for key in final_data:
    for num in final_data[key]:
        total = total + num
second = 0

print(other_dict)
for key,value in other_dict.items():
    if len(value)==1:
        second = second + key
    else:
        row = -1
        index = -1
        for item in value:
            if item[0]==row and (index+1==item[1] or index-1==item[1]):
                continue
            else:
                second = second + key
            row = item[0]
            index = item[1]

print(total)
print(second)


