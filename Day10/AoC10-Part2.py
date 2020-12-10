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
i = 0
chains = []

'''
need to break down to:
difference = 3   - 4 chains (0,1,4,5,6,7) (0,1,4,5,7) (0,1,4,6,7) (0,1,4,7)
difference = 2   - two chains
difference = 1   - just one chain
then multiply the number of chains together
'''

while i < (len(data)-1):
    y=data[i]
    if data[i+1] - data[i] == 1:
        if data[i+2] - data[i] == 2:
            if data[i+3] - data[i] == 3:
                chains.append(4)
                i+=2
            elif data[i+3] - data[i] != 3:
                chains.append(2) 
                i+=1
            #i+=1
        chains = chains
    elif data[i+1] - data[i] == 2:
        chains.append(2)
        i+=1
        chains = chains

    elif data[i+1] - data[i] == 3:
        chains = chains
    i += 1
        

print(reduce(lambda x, y: x*y, chains))

    
'''
I think this is not working because I am skipping any of the elements within data[i+3] - data[i] == 3
'''
# 16777216 is too low