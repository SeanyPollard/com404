#cross_bridge func to count steps and choose response
def cross_bridge(steps):
    for count in range(steps):
        print("Crossed step.")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

#call cross_bridge with input 1
cross_bridge(3)
#call cross_bridge with input 2
cross_bridge(6)
