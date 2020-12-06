with open("Day6\\input6.txt", "r") as data:
    data = [i.replace('\n',',').replace(',','')
            for i in data.read().split('\n\n')]

    charCount = 0
    for i in data:        
        #print(len(set(i)),i)
        charCount+=len(set(i))
    print(charCount)






