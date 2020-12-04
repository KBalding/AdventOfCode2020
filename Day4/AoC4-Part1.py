passports = []
x=0
vCount=0
keys = ["byr:",
        "iyr:",
        "eyr:",
        "hgt:",
        "hcl:",
        "ecl:",
        "pid:"]
        #"cid"]



with open("Day4\\input.txt", "r") as data:
    passports = [i.replace('\n', ' ').replace(':',': ').split()
                 for i in data.read().split('\n\n')]
    for i in passports:
        #print(passports[x])
        check = all(i in passports[x] for i in keys)
        if check:
            print("valid")
            vCount+=1
        else:
            print("invalid")
        x+=1
    print(vCount)
