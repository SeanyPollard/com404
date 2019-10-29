def isFusionShot(type_1,type_2):
    if (type_1 == type_2):
        return True
    else:
        return False

def isDefectiveShot(type_1,type_2):
    fusion = isFusionShot(type_1,type_2)
    if fusion == False:
        if (type_1 == "Infurnus" and type_2 == "AquaBeek") or (type_1 == "AquaBeek" and type_2 == "Infurnus"):
            return True
        else:
            return False
    else:
        return False

def run():
    type_1 = input("Please input a type for your first slug:\n")
    type_2 = input("Please input a type for your second slug:\n")
    shot = input("Please input the shot you wish to attempt, 'fusion' or 'defective':\n")

    if shot == "fusion":
        result = isFusionShot(type_1,type_2)
        if result == True:
            print("This was a fusion shot")
        else:
            print("This was not a fusion shot")
    elif shot == "defective":
        result = isDefectiveShot(type_1,type_2)
        if result == True:
            print("This was a defective shot")
        else:
            print("This was not a defective shot")
    else:
        print("Invalid selection. Please try again")

# Run the program
run()


