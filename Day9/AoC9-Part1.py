with open("Day9\\test.txt","r") as data:
    data = data.readlines()
    data = [i.strip() for i in data]


x = 0
y = 5



while y< len(data):
    current = int(data[y])
    preamble = data[x:y]
    x += 1
    y += 1
    #print(int(preamble[2]) + int(preamble[3]))
    check = int(preamble[2]) + int(preamble[3])
    
    if int(preamble[2]) + int(preamble[3]) == current:
        
        print(check)


    
    #print(preamble,current)