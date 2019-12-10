# Add your code below for question 5.
# Variable initialisation
avengers = 0
loop = 5

# Begin run
print("You have 0 Avengers. Assembling...")

# Begin loop
for count in range(0,loop,1):
    # Request user input and check response
    # Prgrogram acts according to response
    print("Do we have an Avenger?")
    response = input()
    if response == "Yes":
        avengers += 1
        print("An Avenger has been assembled.")
    elif response == "No. A fake.":
        avengers -= 1
        print("We had an imposter in our midst.")
    else:
        print("Better find another.")

# Display result of all responses
print(str(avengers) + " Avengers have been assembled.")