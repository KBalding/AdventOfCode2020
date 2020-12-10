from functools import reduce
with open("Day10\\test.txt","r") as data:
    data = data.readlines()
    data = [int(i.strip()) for i in data]
    data = sorted(data)
    max_ = (max(data)+3)
    data.append(0)
    data.append(max_)
    data = sorted(data)


print(data)
x = 0
chains = []

'''
need to break down to:
difference = 3   - 4 chains (0,1,4,5,6,7) (0,1,4,5,7) (0,1,4,6,7) (0,1,4,7)
difference = 2   - two chains
difference = 1   - just one chain
then multiply the number of chains together
'''

for i in range(len(data)-1):
    y=data[x]
    if data[x+1] - data[x] == 1:
        if data[x+2] - data[x] == 2:
            if data[x+3] - data[x] == 3:
                chains.append(4)
                x+=2
            elif data[x+3] - data[x] != 3:
                chains.append(2) 
                x+=1  
        chains = chains
    elif data[x+1] - data[x] == 2:
        if data[x+2] - data[x] == 1:
            chains.append(2)
            x+=1
        chains = chains

    elif data[x+1] - data[x] == 3:
        chains = chains
    x += 1
        

print(reduce(lambda x, y: x*y, chains))

    
