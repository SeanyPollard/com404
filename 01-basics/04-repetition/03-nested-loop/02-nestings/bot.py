#Ask user for sequence and markers
string = input("Please enter a sequence\n")
marker = input("Please enter the character for the marker\n")

#init vars
pos1 = 0
pos2 = 0
poscount = 0

#for and while to find character from start
for count in string:
    poscount += 1
    if count == marker:
        if pos1 > 0:
            pos2 = poscount
        else:
            pos1 = poscount

#calc distance
finalpos = abs(pos2 - pos1) - 1

#completion statement
print("The distance between markers is " + str(finalpos))

