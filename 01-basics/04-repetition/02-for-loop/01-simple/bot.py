#Ask user for a number
num = int(input("How many mountains should I display?\n"))

#Init statement
print("\nDisplaying...\n")

#For loop to print mountains
for count in range(num):
    print("""
           __
          /  \\_
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\\n""")

#Completion statement
print("Done!")