passports = []
x=0
vCount=0
keys = {"byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"}




with open("Day4\\test2.txt", "r") as data:
    passports = [i.replace('\n', ' ').split()
                 for i in data.read().split('\n\n')]
    for i in passports:
        print(i)
        print(i[0:1])






print(keys)
    # for i in passports:
    #     #print(passports[x])
    #     x+=1
    # print(vCount)
