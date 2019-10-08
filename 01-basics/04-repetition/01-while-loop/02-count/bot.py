#Ask user for number of cables to remove
cables = int(input("How many live cables should I avoid?\n"))

#Initialise counter
counter = 0

#While less than input cables, keep avoiding
while counter < cables:
    counter += 1
    print("Avoiding... Done! " + str(counter) + " live cables avoided.")

#Completion statement
print("All live cables have been avoided!")
