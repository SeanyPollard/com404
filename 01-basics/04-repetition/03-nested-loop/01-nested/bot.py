#Ask user for number of rows and columns
rows = int(input("How many rows should I have?\n"))
columns = int(input("How many columns should I have?\n"))

#init statement and vars
print("Here I go:")
smiley = "=D "

#for loop through rows and nest columns
for rowcount in range(rows):
    printed = ""
    for colcount in range(columns):
        printed += smiley
    print(printed)

#completion statement
print("Done!")
