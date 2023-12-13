with open('inputs\day4_input.txt') as f:
    text = f.read()
text = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
"""
a = {1:1,2:1,3:1,4:1}
>>> for key in a:
	matches = 3
	for i in range(key+1,key+matches+1):
		a[i] = a[i]+a[key]*matches
		print(a[i])
		print(a)

		
4
{1: 1, 2: 4, 3: 1, 4: 1}
4
{1: 1, 2: 4, 3: 4, 4: 1}
4
{1: 1, 2: 4, 3: 4, 4: 4}
16
{1: 1, 2: 4, 3: 16, 4: 4}
16
{1: 1, 2: 4, 3: 16, 4: 16}
""" ##testing
alist = text.split('\n')
adict = {int(x[4:x.find(':')].strip()):[x[x.find(':')+1:],1] for x in alist}
print(adict)

def score_game(win_num,my_num):
    win_num = win_num.strip().split(' ')
    win_num = [int(x) for x in win_num if x!='']
    my_num = my_num.strip().split(' ')
    my_num = [int(x) for x in my_num if x!='']
    count = 0 
    for my in my_num:
        #print(my, '-',win_num, my in win_num)
        if my in win_num:
            count = count + 1
    return count
score = 0 
for line in alist:
    line = line[line.find(':')+1:].split('|')
    game_score = score_game(line[0],line[1])
    score = score + game_score
print(score)

#part 1
'''alist = text.split('\n')
# adict = {int(x[4:x.find(':')].strip()):[x[x.find(':')+1:],1] for x in alist}
# print(adict)
#game = alist[0][alist[0].find(':')+1:].split('|')
#win = game[0].strip().split(' ')
#num = game[1].strip().split(' ')

def score_game(win_num,my_num):
    win_num = win_num.strip().split(' ')
    win_num = [int(x) for x in win_num if x!='']
    my_num = my_num.strip().split(' ')
    my_num = [int(x) for x in my_num if x!='']
    count = 0 
    for my in my_num:
        #print(my, '-',win_num, my in win_num)
        if my in win_num:
           # print(count)
            if count ==0: count = 1
            else: count = count*2
            #count = count + 1
    return count
score = 0 
for line in alist:
    line = line[line.find(':')+1:].split('|')
    game_score = score_game(line[0],line[1])
    score = score + game_score
print(score)''' #part 1