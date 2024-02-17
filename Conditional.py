# indetation - Proper Spacing 

#------------------ if elif Else -------------#

light = input("What is the colour of light form (Green,Red,Yellow)")

if (light == "Green"):
    print("You can go")
elif (light == "Red"):
    print("You have to Stop ")
elif (light == "Yellow"):
    print("Watch and Go")
else:
    ("The light is not working or showing wrong colour")
    





#----------------------------------------
marks = int(input("Write down your marks"))

if (marks >= 90):
    print("Your grade is A ")

elif ( marks >=80 and marks <= 90 ):
    print("Your grade is 'B'")
elif(marks >=70 and marks <= 80):
    print("your grade is 'C'")
elif(marks >=40 and marks <= 70):
    print("your grade is 'D'")
else:
    print("you are fail")


# nesting - To add if inside a if 