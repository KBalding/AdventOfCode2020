import itertools

with open("Day9/input.txt","r") as data:
    data = data.readlines()
    data = [int(i.strip()) for i in data]


def checkP(numbers, length, target):
    iterable = itertools.permutations(numbers,length)
    predicate = lambda x: (sum(x) == target)
    vals = filter(predicate,iterable)
    
    #print(list(vals),target)
    if list(vals) == []:
        print(target)
        
x = 0
y = 25

while y< len(data):
    current = int(data[y])
    preamble = data[x:y]
    x += 1
    y += 1
    #print(int(preamble[2]) + int(preamble[3]))
    checkP(preamble, 2, current)
    
    # if int(preamble[2]) + int(preamble[3]) == current:
    #     print(check)