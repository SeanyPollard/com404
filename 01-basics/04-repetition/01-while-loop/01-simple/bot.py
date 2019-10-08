#Ask user for number of cables to remove

cables = int(input("How many cables should I remove?\n"))

#While more than 0 cables, keep removing
while cables > 0:
    print("Removed cable.")
    cables -= 1
