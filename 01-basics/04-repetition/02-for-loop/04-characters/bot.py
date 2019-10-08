#Ask user for a word
text = input("What strange markings do you see?\n")

#loop through chars and print
for count in range(0,len(text),1):
    print("index " + str(count) + ": " + text[count])

#completion statement
print("Done!")