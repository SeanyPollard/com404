#Ask user to input a number
number = int(input("Please enter a number\n"))

#Init vars
count = 0
total = 1

#while loop factorial calculation
while count < number:
    count += 1
    total *= count

#Completion statement
print("The factorial is " + str(total))