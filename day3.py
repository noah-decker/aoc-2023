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
.664.598..'''

special_char = "*"
alist = text.split("\n")
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
total = 0
def replace_num(string,start,stop):
    string_list = list(string)
    string_list[start:stop+1] = len(string_list[start:stop+1])*'.'
    new_string = "".join(string_list)
    return new_string
print(strlen)
print(listlen)
for list_index in range(0,listlen):
    for str_index in range(0,strlen):
        if alist[list_index][str_index] in special_char:
            list_min = 0
            list_max = listlen-1
            str_min = 0
            str_max = strlen-1
            check_up = (max(list_index-1,list_min),str_index)
            check_right = (list_index,min(str_max,str_index+1))
            check_left = (list_index,max(str_min,str_index-1))
            check_down = (min(list_index+1,list_max),str_index)
            check_up_right = (max(list_index-1,list_min),min(str_max,str_index+1))
            check_up_left = (max(list_index-1,list_min),max(str_min,str_index-1))
            check_down_left = (min(list_index+1,list_max),max(str_min,str_index-1))
            check_down_right = (min(list_index+1,list_max),min(str_max,str_index+1))
            check_list = [check_up,check_right,check_left,check_down,check_up_right,check_up_left,check_down_left,check_down_right]
            first_num = []
            second_num = []
            for check in check_list:
                l,s = check
                #print(list_index,str_index)
                #print(check,alist[l][s])
                if alist[l][s].isdigit():
                    # print(l,s,alist[l][s])
                    # print(find_num(s,alist[l]))
                    num,start,stop = find_num(s,alist[l])
                    #print(num,start,stop)
                    if first_num == []:
                        first_num = [num,start,stop]
                        #print(first_num)
                    elif first_num != [] and first_num != [num,start,stop] and second_num ==[]:
                        second_num = [num,start,stop]
                       # print(first_num,second_num)
                        string = replace_num(alist[l],first_num[1],first_num[2])
                        alist[l] = string
                        string = replace_num(alist[l],second_num[1],second_num[2])
                        alist[l] = string
                        total = total + (int(first_num[0])*int(second_num[0]))
                    # else:
                    #     first_num = []
                    #     second_num = []
                    
              
print(total)


# part 1
# special_char = "!@#$%^&*()\{\}[]=+:;<>,`~\\?/|_-'\""
# alist = text.split("\n")
# strlen = len(alist[0])
# listlen = len(alist)
# def find_num(j,string):
#     if string[j].isnumeric():

#         start = j
#         end = j
#         while True:
#             if start>0 and string[start-1].isnumeric():
#                 start = start-1
#             elif end<=len(string)-2 and string[end+1].isnumeric():
#                 end = end + 1
#             else:
#                 break
#         return string[start:end+1],start, end
#     else:
#         return ''
# total = 0
# def replace_num(string,start,stop):
#     string_list = list(string)
#     string_list[start:stop+1] = len(string_list[start:stop+1])*'.'
#     new_string = "".join(string_list)
#     return new_string
# print(strlen)
# print(listlen)
# for list_index in range(0,listlen):
#     for str_index in range(0,strlen):
#         if alist[list_index][str_index] in special_char:
#             list_min = 0
#             list_max = listlen-1
#             str_min = 0
#             str_max = strlen-1
#             check_up = (max(list_index-1,list_min),str_index)
#             check_right = (list_index,min(str_max,str_index+1))
#             check_left = (list_index,max(str_min,str_index-1))
#             check_down = (min(list_index+1,list_max),str_index)
#             check_up_right = (max(list_index-1,list_min),min(str_max,str_index+1))
#             check_up_left = (max(list_index-1,list_min),max(str_min,str_index-1))
#             check_down_left = (min(list_index+1,list_max),max(str_min,str_index-1))
#             check_down_right = (min(list_index+1,list_max),min(str_max,str_index+1))
#             check_list = [check_up,check_right,check_left,check_down,check_up_right,check_up_left,check_down_left,check_down_right]
#             for check in check_list:
#                 l,s = check
#                 if alist[l][s].isdigit():
#                     # print(l,s,alist[l][s])
#                     # print(find_num(s,alist[l]))
#                     num,start,stop = find_num(s,alist[l])
#                     string = replace_num(alist[l],start,stop)
#                     alist[l] = string
#                     total = total + int(num)
              
# print(total)