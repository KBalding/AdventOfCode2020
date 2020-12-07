myDict = {'light red bags ': [' 1 bright white bag, 2 muted yellow bags.'], 'dark orange bags ': ' 3 bright white bags, 4 muted yellow bags.', 'bright white bags ': [' 1 shiny gold bag.'], 'muted yellow bags ': ' 2 shiny gold bags, 9 faded blue bags.', 'shiny gold bags ': ' 1 dark olive bag, 2 vibrant plum bags.', 'dark olive bags ': ' 3 faded blue bags, 4 dotted black bags.', 'vibrant plum bags ': ' 5 faded blue bags, 6 dotted black bags.', 'faded blue bags ': ' no other bags.', 'dotted black bags ': ' no other bags.'}

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

#Checking if string 'Mary' exists in dictionary value
print(search(myDict, 'shiny')) #prints firstName




#this only works if the values in the dictionary are in a list []
#I need to work out how to make my test.py create the dictionary values in a list, not a string.