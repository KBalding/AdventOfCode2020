map=[]
with open("Day3\Aoc3.txt", "r") as data:
    map = data.readlines()
    map = [line.strip() for line in map]

#print(map)

tree = '#'
treeCount = 0
x = 0
y = 0


while y+1 < len(map):
    x+=3
    y+=1
    position = map[y][x % len(map[y])]
    #print(position)
    if position == '#':
        treeCount+=1
print(treeCount)