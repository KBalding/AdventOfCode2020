accumulator = 0

with open('Day8\\test.txt') as data:
    data = data.readlines()
    data = [line.strip() for line in data]





for i in data:
    operator, direction = (i.split(' '))
    print(int(direction))






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