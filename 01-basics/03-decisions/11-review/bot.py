# Ask what the user's name is
first_name = input("What's your name?\n")

#Check name and respond accordingly
if first_name == "Seany":
    print("Oh that's a sick name!")
else:
    print("Nice to meet you " + first_name)

#Ask for surname
surname = input("What's your surname?\n")

#Check first and surname
if first_name == "Seany" and surname == "Pollard":
    print("OMG you're a legend!")
elif first_name == "Paris" and surname == "Hall":
    print("Cool, cool.")
elif (first_name == "Murray" and surname == "Creese") or (first_name == "Lewis" and surname == "Templeton") or (first_name == "Steve" and surname == "Smith"):
    print("Fuck you traitors")
else:
    print("Okay.")

#Ask user for age
age = int(input("How old are you?"))

#Check and respond
if age < 30:
    if age % 2 == 1:
        print("You're young and odd")
    else:
        print("You're young")
elif age >= 30:
    if first_name == "Seany" and surname == "Pollard":
        print("You're super cool")
    else:
        print("You're probs alright")
else:
    print("You literally can't be that age")

