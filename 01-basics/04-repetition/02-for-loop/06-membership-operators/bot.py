#Ask user for a phrase
text = input("What phrase do you see?\n")

#init var and statement
phrase = ""
print("Reversing...")

#loop through chars to reverse
for count in text:
    phrase = count + phrase

#completion statement
print("The phrase is: " + phrase)