# # indetation - Proper Spacing 

# #------------------ if elif Else -------------#

# light = input("What is the colour of light form (Green,Red,Yellow)")

# if (light == "Green"):
#     print("You can go")
# elif (light == "Red"):
#     print("You have to Stop ")
# elif (light == "Yellow"):
#     print("Watch and Go")
# else:
#     ("The light is not working or showing wrong colour")
    





# #----------------------------------------
# marks = int(input("Write down your marks"))

# if (marks >= 90):
#     print("Your grade is A ")

# elif ( marks >=80 and marks <= 90 ):
#     print("Your grade is 'B'")
# elif(marks >=70 and marks <= 80):
#     print("your grade is 'C'")
# elif(marks >=40 and marks <= 70):
#     print("your grade is 'D'")
# else:
#     print("you are fail")


# # nesting - To add if inside a if 

#--------------------Solving some Question in Conditional Statement ----------------------#


# 1. WAP to check the number entered by the user is odd or even 
# Number1 = int(input("Add any Number: "))
# Rem = Number1 % 2  

# if (Rem == 0):
#     print("Your NUmber is Even ")
# else:
#     print("Your number is Odd")


# 2 WAP TO Find the greatest of 3 number entered by the user
# Number1 = int(input("Write down any Number")) 
# Number2 = int(input("Write down any Number")) 
# Number3 = int(input("Write down any Number")) 

# if (Number1 > Number2) and (Number1>Number3):
#     print("Number 1 is the Greatest Number")
# elif(Number2 > Number1) and (Number2>Number3):
#      print("Number 2 is the greatest Number")
# else:
#      print("Number 3 is the greatest Number")




# 3 To check if  a number is  a multipal of 7 or not 
# Number1 = int(input("Write Down any Number"))
# Rem = Number1 % 7
# if (Rem == 0):
#     print("This is a Multipal of 7")
# else:
#     print("This is Not a multipal of 7")


#4 WAP to display Hello if the number is div of 5 if not then print Bye 

# Num1 = int(input("Write donw any number"))
# rem = Num1 % 5 

# if(rem==0):
#     print("Hello")
# else: 
#     print("BYE")


# WAP To write a program to write a Program to calculate the eelctricty 

# amt = 0

# unit = int(input("Put down the unit"))

# if unit <= 100:
#     print("Your bill is less than 100.So, no charge")
# elif(unit> 100) and(unit<200):
#     amt = (unit - 100) * 5
# else:
#     amt = 500 + (unit - 200)* 10

# print(amt)


# WAP to display the last digit of a number. 

Num = int(input("Enter any number"))
print("last Digit of number is ",Num%10)

