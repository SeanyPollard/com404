# input destination
look = input("Where should I look?\n")
#if statement
if look == "in the bedroom":
    bedroom = input("Where in the bedroom should I look?\n")
    #inbedded if
    if bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
#else if statement
elif look == "in the bathroom":
    bathroom = input("Where in the bathroom should I look?\n")
    #inbedded if
    if bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")
#else if statement
elif look == "in the lab":
    lab = input("Where in the lab should I look?\n")
    #inbedded if
    if lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
#final statement
else:
    print("I do not know where that is but I will keep looking.")