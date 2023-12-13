with open('inputs\day3_input.txt') as f:
    text = f.read()
atext = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

special_char = "!@#$%^&*()\{\}[]=+:;<>,`~\\?/|_-'\""
alist = text.split("\n")
alist.pop()
strlen = len(alist[0])
listlen = len(alist)
def find_num(j,string):
    if string[j].isnumeric():

        start = j
        end = j
        while True:
            if start>0 and string[start-1].isnumeric():
                start = start-1
            elif end<=len(string)-2 and string[end+1].isnumeric():
                end = end + 1
            else:
                break
        return string[start:end+1],start, end
    else:
        return ''
def make_index_range(string,start,end):
    start = start-1 if start-1>=0 else 0
    end = end+1 if end+1<=len(string)-1 else len(string)-1
    return [x for x in range(start,end+1)]
def check_symbols(strlist,list_index,start,end):
    string = strlist[list_index]
    index_range = make_index_range(string,start,end)
    #print('cs',list_index,start,end)
    if (start>0 and string[start-1] in special_char):
        return True
    elif(end<len(string)-1 and string[end+1] in special_char):
        return True
    else: 
        if list_index == 0:
            for i in index_range:
                if strlist[list_index+1][i] in special_char:
                    return True
            return False
        elif list_index == len(strlist)-1:
            for i in index_range:
                if strlist[list_index-1][i] in special_char:
                    return True
            return False
        else:
            for i in index_range:
                #print(list_index,i,strlist)
                if strlist[list_index+1][i] in special_char or strlist[list_index-1][i] in special_char:
                    return True
            return False
total = 0
print(listlen,strlen)
for list_index in range(0,listlen):
    end = -1
    for str_index in range(0,strlen):
        print(str_index , f'end: {end}  {alist[list_index][str_index]}')
        if str_index > end:
            #print(f'end = {end}')
            print(f'end: {end}  {alist[list_index][str_index]}')
            if (alist[list_index][str_index]).isnumeric():
                string, start, temp_end = find_num(str_index,alist[list_index])
                #print(list_index,start,end,temp_end)
                print(f'number: {string} cs: {check_symbols(alist,list_index,start,temp_end)}')
                if check_symbols(alist,list_index,start,temp_end):
                    print(int(string))
                    total = total + int(string)
                    end = temp_end
        else:
            continue
print(total)                


                


