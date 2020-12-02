
list =[]
with open("Day2\AoC2.txt","r") as data:
    for row in data:
        list.append(row.strip())

# list =[
#     "1-3 a: abcde"
#      ,"1-3 a: abade"
#     ,"3-4 l: lljllll"
#     ,"1-5 k: kkkkhkkkkkkkkkk"
#         ,"1-3 b: cdefg"
#         ,"2-9 c: ccccccccc"]


totalCount=0

for a in list:
    x,y = a.split(':')
    y=y.strip()
    #print(x)
    countRange,char = x.split(" ")
    pos1,pos2 = countRange.split('-',1)
    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    #print(pos1,pos2,char)
    #print(y.find(char))
    indices = [i for i, a in enumerate(y) if a == char]
    #print(indices)
    if pos1 in indices and pos2 in indices:
        pass
    elif pos1 in indices:
       # print (a,pos1)
        totalCount+=1
    elif pos2 in indices:
       # print (a,pos2)
        totalCount+=1
print(totalCount)











