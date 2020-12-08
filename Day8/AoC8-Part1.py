with open('Day8\\input.txt') as data:
    data = data.readlines()
    data = [line.strip() for line in data]

    
    accumulator = 0
    currentIndex = 0
    checked = set()



while currentIndex <= len(data):  
    if currentIndex in checked:
        print(accumulator)
        #print(checked)
        break
    #print(checked)
    checked.add(currentIndex)
    operation = data[currentIndex].split()
    if operation[0] == 'acc':
        #print(int(direction))
        #print(accumulator)
        accumulator+=int(operation[1])
        currentIndex += 1        
    elif operation[0] == 'nop':
        #print(int(direction))
        currentIndex += 1       
    elif operation[0] == 'jmp':
        #print(int(direction))
        currentIndex += int(operation[1])
    else:
        print('ERROR')
       
print(checked)




'''
need to iterate through list, increase/decrease index position
based on direction value. 
if operator == 'acc' then add direction value to accumulator, carry on iteration
if operator == 'nop' ignore direction, carry on iteration
if operator == 'jmp' increase/decrease next iteratation by that amount
if index has been hit before, break and return accumulator
NB. need to keep track of checked index;
if current index not in checked, add to checked
else return accumulator and break
'''