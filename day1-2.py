with open('inputs\day1_input.txt') as f:
    testinput = f.read()
num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def rfindfunc(word):
	maxnum=''
	maxindex = -1
	for item in num:
		index = word.rfind(item)
		if index!=-1 and index>maxindex:
			maxnum = item
			maxindex = index
	return maxnum

def findfunc(word):
	maxnum=''
	maxindex = float("inf")
	for item in num:
		index = word.find(item)
		if index!=-1 and index<maxindex:
			maxnum = item
			maxindex = index
	return maxnum
numdict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
total = 0
for line in testinput.split('\n'):
    first = findfunc(line)
    last = rfindfunc(line)
    if not first.isnumeric():
        first = numdict[first]
    if not last.isnumeric():
        last = numdict[last]
    number = int(first+last)
    total = total + number
print(total)

    
