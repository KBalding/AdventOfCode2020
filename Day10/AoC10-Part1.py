with open("Day10\\input.txt","r") as data:
    data = data.readlines()
    data = [int(i.strip()) for i in data]
    data = sorted(data)
    max_ = (max(data)+3)
    data.append(0)
    data.append(max_)
    data = sorted(data)


print(data)
x = 0
jolt1 = 0
jolt3 = 0


for i in range(len(data)-1):
        if data[x+1] - data[x] == 1:
            jolt1 +=1
            #print(jolt1, data[x], data[x+1])
        elif data[x+1] - data[x] == 3:
            jolt3 +=1
            #print(jolt3, data[x], data[x+1])
        x += 1
answer = jolt1 * jolt3
print('jolt1: ',jolt1, '\njolt3: ',jolt3, '\nanswer: ',answer)

