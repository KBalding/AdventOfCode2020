with open("Day22\\input.txt", "r") as data:
    data = data.read().replace("Player","").replace(":","")



p1, p2 = data.split('\n\n')



p1 = p1.split()
p2 = p2.split()

key = p1.pop(0)
key = p2.pop(0)

for i in range(0, len(p1)): 
    p1[i] = int(p1[i]) 
for i in range(0, len(p2)): 
    p2[i] = int(p2[i]) 


i=1 
while len(p1) >0 and len(p2) >0:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
        # p1.pop(0)
        # p2.pop(0)
        #break
    elif c1 < c2:
        p2.append(c2)
        p2.append(c1)
        # p1.pop(0)
        # p2.pop(0)
        #break
    i+=1
print("rounds",i)
score = 0
if len(p1) > 0:
    for i in range(len(p1)):
        score = score + (len(p1) - i) * p1[i]
else:
    for i in range(len(p2)):
        score = score + (len(p2) - i) * p2[i]

print(score)



