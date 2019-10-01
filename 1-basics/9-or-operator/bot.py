# Ask user for adventure type
ad_type = input("Which type of adventure is this?\n")

# Check type and respond accordingly
if ad_type == "scary" or "short":
    print("Entering the dark forest!")
elif ad_type == "safe" or "long":
    print("Taking the safe route!")
else:
    print("I'm notsure where to go!")