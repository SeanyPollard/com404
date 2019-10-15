#func to cal if ladd climbed
def climb_ladder(rem, cross):
    if rem < cross:
        print("Still some way to go!")
    else:
        print("We made it!")

#call func with input 1
climb_ladder(2, 5)
#call fun with input 2
climb_ladder(5, 5)
