#Ask user for a phrase
phrase = input("Please enter a phrase\n")

#Initialise bop
bop = "Bop "
statement = bop

#Initialise counter
counter = 1

#While less than input bars, keep charging
while counter < len(phrase):
    counter += 1
    statement += bop

#Completion statement
print(statement)
