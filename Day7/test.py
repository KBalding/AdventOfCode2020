# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.

with open("Day7\\test7.txt", "r") as data:
    data = data.readlines()
    #data = [line.strip() for line in data]
    key = [data.split('contain',1)[0].strip() for data in data] 
    value = [i.split('contain',1)[1].strip() for i in data]




bags = dict(zip(key,[value]))
print('\n\n',key)
print('\n\n',value)
print('\n\n',bags)




# Both keys and values seem to print out OK, but when creating a dictionary from them all values are being assined to first key?

