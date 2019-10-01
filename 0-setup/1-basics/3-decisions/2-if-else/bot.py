# ask user for activity input
act_type = input("Please enter the activity to be completed.")

# check activity input and respond accordingly
if act_type == "Calculate":
    print("Performing calculations...")
else:
    print("Performing " + act_type + "...")

# tell user complete
print("Activity completed!")