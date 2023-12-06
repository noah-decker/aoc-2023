with open('inputs\day2_input.txt') as f:
    text = f.read()
alist = [x[x.find(':')+2:] for x in text.split('\n')]
def get_num(word):
    return int(word[4:])
blist = [get_num(x[:x.find(':')]) for x in text.split('\n')]
gamedict = dict(zip(blist,alist))

def fun(alist):
    green = 0
    red = 0
    blue = 0
    
    for dice in alist.split(','):
        if 'red' in dice and int(dice.strip().split(' ')[0])>red:
            red = int(dice.strip().split(' ')[0])
        elif 'blue' in dice and int(dice.strip().split(' ')[0])>blue:
            blue = int(dice.strip().split(' ')[0])
        elif 'green' in dice and int(dice.strip().split(' ')[0])>green:
            green = int(dice.strip().split(' ')[0])
    
    return red,blue,green
total = 0
for key in gamedict:
    red,blue,green = 0,0,0
    for draw in gamedict[key].split(';'):
        r1,b1,g1 = fun(draw)
        if r1> red:
            red = r1

        if b1>blue:
            blue = b1

        if g1>green:
            green = g1
    power = red*blue*green
    total = total+power

print(total)

 #Part 1 below   
'''    
def fun(alist):
    green = 13
    red = 12
    blue = 14
    oneover = False
    for dice in alist.split(','):
        if 'red' in dice and int(dice.strip().split(' ')[0])>red:
            oneover = True
        elif 'blue' in dice and int(dice.strip().split(' ')[0])>blue:
            oneover = True
        elif 'green' in dice and int(dice.strip().split(' ')[0])>green:
            oneover = True
    
    return oneover

total = 0
for key in gamedict:
    oneover = False
    for draw in gamedict[key].split(';'):
        if fun(draw):
            oneover = True
    if oneover:
        total = total 
    else:
        total = total +key

print(total)'''
