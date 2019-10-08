#Ask user for number of numbers to sum
numbers = int(input("How many numbers should I sum up?\n"))

#Initialise vars
count = 0
total = 0

#loop through input number of times to sum
while count < numbers:
    count += 1
    total += int(input("Please enter number " + str(count) + " of " + str(numbers) +":\n"))

#Completion statement
print("The answer is " + str(total))