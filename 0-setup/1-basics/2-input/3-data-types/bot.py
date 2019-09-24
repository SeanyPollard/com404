# Teach Beep the robo boi who you are, how old and let him work out your BMI
#Beep intros himself and asks who you are
print("S\'up. I'm Beep the robo boi. What\'s your name?")
name = input()
print("Safe. I always wanted to know a " + name + "! How many rotations of the star have you survived?")
age = int(input())
print("Woaaaah! " + str(age) + " years! That's so many. Please tell me your height in meters " + name)
height = float(input())
print("Okay and how many kilos do you consist of? I promise I won't call you fat.")
weight = float(input())
bmi = weight / (height*height)
print("So, " + name + ", you're " + str(age) + "yrs old and have a BMI of " + str(round(bmi,1)))