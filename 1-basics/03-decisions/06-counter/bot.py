# Ask user for number 1
num_1 = int(input("Please input your first number:\n"))

# Ask user for number 2
num_2 = int(input("Please input your second number:\n"))

# Ask user for number 3
num_3 = int(input("Please input your third number:\n"))

# Init even and odd counters
even_count = int(0)
odd_count = int(0)

# Check numbers and add results to counters
if num_1 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
if num_2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
if num_3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

# Output result to user
print("There were " + str(even_count) + " even and " + str(odd_count) + " odd numbers.")
