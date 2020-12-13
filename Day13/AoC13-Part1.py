with open('Day13\\input.txt','r') as data:
    data = data.read().replace('x,','').replace('\n',',')
    #data = data.readlines()
    #data = data.strip()
    data = data.split(',')
    #data = [data.replace('x,','').strip() for data in data]
    #data = [int(i.strip()) for i in data]
    


print(data)

time = data[0]
bus = data[1:]
buses = []
busID = []


# for i in bus:
#     print(int(i))


for i in bus:
    cm = (int(time)//int(i))

    previousbus = int(i)*int(cm)
    #print(previousbus)

    nextbus = int(previousbus) + int(i)
    buses.append(int(nextbus))
    busID.append(int(i))
    print('bus',i,'nextbus',nextbus)

earliestBus =(min(buses))
waitTime = (earliestBus-int(time))
busIDIndex = (buses.index(earliestBus))
earliestBusID = (busID[busIDIndex])

answer = waitTime * earliestBusID
print(answer)