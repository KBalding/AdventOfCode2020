
list =[]
with open("Day2\AoC2.txt","r") as data:
    for row in data:
        list.append(row.strip())

testList =[
    "1-3 a: abcde"
        ,"1-3 b: cdefg"
        ,"2-9 c: ccccccccc"]

newDict={}
totalCount=0

for a in list:
    x,y = a.split(':')
    y=y.strip()
    #print(x)
    countRange,char = x.split(" ")
    pmin,pmax = countRange.split('-',1)
    pmin = int(pmin)
    pmax = int(pmax)
    #print(pmin,pmax,char)
    for z in y:
        characters={}
        for character in y:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] =  1
    #print(characters,char)
    if char in characters:
        if pmin <= characters[char] <=pmax:
            totalCount =totalCount+1
            #print(characters[char])
    else:
        pass
print(totalCount)








