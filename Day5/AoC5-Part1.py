test = 'FBFBBFFRLR'
test2 = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL','FFBBBBFRRR']


maxID = 0
max1 = []
with open("Day5\input.txt","r") as data:

    for i in data:
        seat = i.strip().replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        seatID = 8*int(seat[:7],2) + int(seat[-3:],2)
        max1.append(seatID)
        if seatID > maxID:
            maxID = seatID
    print("seats=",len(max1))
    print("maxID=",maxID)





# def binarySearch(sequence, item):
#     maxrows = len(sequence) -1
#     minrows = 0
#     while minrows <= maxrows:
#         midpoint = minrows + (maxrows - minrows)//2
#         midpointValue = sequence[midpoint]
#         if midpointValue == item:
#             return midpoint
#         elif item < midpointValue:
#             maxrows = midpoint -1
#         else:
#             minrows = midpoint +1
#     return None

# sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
# item_a = 4

# print(binarySearch(sequence_a,item_a))
