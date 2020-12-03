map=[]
with open("Day3\Aoc3.txt", "r") as data:
    map = data.readlines()
    map = [line.strip() for line in map]

#print(map)

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
totalTrees = []
for slopes in slopes:
    tree = '#'
    treeCount = 0
    x = 0
    y = 0
    


    while y+1 < len(map):
        x+=slopes[0]
        y+=slopes[1]
        position = map[y][x % len(map[y])]
        #print(position)
        if position == '#':
            treeCount+=1
    totalTrees.append(treeCount) 
#print(totalTrees)


i=1
for x in totalTrees:
    i = i * x
print(i)