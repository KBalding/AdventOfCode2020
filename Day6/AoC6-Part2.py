with open("Day6\\input6.txt", "r") as data:
    data = [i 
            for i in data.read().split('\n\n')]
    
    charCount = 0
    for i in data:    
        characters = set('abcdefghijklmnopqrstuvwxyz')
        for a in i.splitlines():
            characters = characters.intersection(a)
        print(characters,len(characters))
            #print(len(set(i)),i)
        charCount+=len(characters)
    print(charCount)







