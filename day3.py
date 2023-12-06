text = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
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
    return [current_index-1,current_index,current_index+1]
data = dict(zip(range(len(text.split('\n'))),text.split('\n')))
new_data = {x:[] for x in range(len(text.split('\n')))}
#print(get_digits('467..114..',5))
#print(get_digits('467..114..',6))
#print(data)

for key in data:
    for index in range(len(data[key])):
        char = data[key][index]
        if char in "!@#$%^&*(){}[]=+:;<>,`~":
            checklist = get_indexs(index)
            for check in checklist:
                if key>0:
                    above = get_digits(data[key-1],check)
                    if above!='':
                        new_data[key-1].append(int(above))
                if key!=len(data)-1:
                    below = get_digits(data[key+1],check)
                    if below!='':
                        new_data[key+1].append(int(below))
                if check != index:
                    same_row = get_digits(data[key],check)
                    if same_row!='':
                        new_data[key].append(int(same_row))
final_data = {key:set(value) for key,value in new_data.items()}

total = 0
for key in final_data:
    for num in final_data[key]:
        total = total + num



