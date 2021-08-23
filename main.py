reqs = set(["COMP 210", "COMP 211", "COMP 301", "COMP 311", "COMP 283","COMP 455","COMP 550"])
additional = set(["MATH 231", "MATH 232", "MATH 233", "MATH 347", "STOR 435"])

labScience = [["ASTR 101","ASTR 101L"], ["BIOL 101","BIOL 101L"]]
otherScience = ["BIOL 202", "PHYS 118"]

mine = ["COMP 210", "COMP 212", "COMP 301", "COMP 311", "COMP 283","COMP 455","COMP 550", "COMP 585", "MATH 233","BIOL 101L", "BIOL 101", "PHYS 118"]
taken = set(mine)

print(reqs)

def checkCore():
    return reqs.difference(taken)

def checkAdditional():
    return additional.difference(taken)

def checkScience():
    count = 0
    science = []

    for i in labScience:
        if i[0] in taken and i[1] in taken:
            count += 1
            science.append([i[0], i[1]])
    
    for i in otherScience:
        if i in taken:
            count += 1
            science.append(i)
    print(count)
    
    return science
    
def checkElectives():
    count = 0
    out = []

    for i in mine:
        char = ''.join(filter(str.isalpha, i))
        num = ''.join(filter(str.isdigit, i))

        if char == "COMP" and int(num) > 420 and i not in reqs:
            count += 1
            out.append(i)

    return out

def checkCOMP():
    left = 0
    left += len(checkCore())
    left += len(checkAdditional())
    sci = len(checkScience())
    if sci > 2:
        sci = 2
    else:
        sci = 2 - sci
    left += sci

    return f"""\nUNC BS Computer Science:\nCan finish in {left} Classes\nCore Needed: {checkCore()}\nElectives Needed: {checkAdditional()}\nScience Needed: {sci}\n"""

print(checkCOMP())