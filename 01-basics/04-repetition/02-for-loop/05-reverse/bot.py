#Ask user for a phrase
text = input("What phrase do you see?\n")

#init var and statement
phrase = ""
print("Reversing...")

#loop through chars to reverse
for count in range(len(text),0,-1):
    phrase += text[count-1]

#completion statement
print("The phrase is: " + phrase)