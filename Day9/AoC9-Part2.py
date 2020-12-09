# two or more numbers next to each other summed = 507622668
# in the test data, the numbers 15,25,47,40 = 127 (no were looking for)
# once found the sequence, add the first and last value for the answer

import itertools

with open("Day9/test.txt","r") as data:
    data = data.readlines()
    data = [int(i.strip()) for i in data]

sumof = 0


for i in data:
    sumof +=i
    if sumof > 127:
        break
    elif sumof == 127:
        print(i)




# def checkP(numbers, length, target):
#     iterable = itertools.permutations(numbers,length)
#     predicate = lambda x: (sum(x) == target)
#     vals = filter(predicate,iterable)
    
#     #print(list(vals),target)
#     if list(vals) == []:
#         print(target)
        
# x = 0
# y = 25

# while y< len(data):
#     current = int(data[y])
#     preamble = data[x:y]
#     x += 1
#     y += 1
#     #print(int(preamble[2]) + int(preamble[3]))
#     checkP(preamble, 2, current)
    
#     # if int(preamble[2]) + int(preamble[3]) == current:
#     #     print(check)`