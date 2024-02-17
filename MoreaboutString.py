# # ------------------Basic opertation in String-------------------------

# --------------Concatenation  and Lenght Operation ------------------------

# Name1 = "Sailesh"
# Name2 = "Aryal"
# Full_name = Name1 +" "+ Name2


# print(Full_name)
# print(len(Name1))
# print(len(Full_name))



#------------------------------Indexing & slicing -------------------------------


# indexing is used to know the Location of a particular String Word

# My_name = "Sailesh Aryal"
# print(My_name[3])

# print(My_name[1])
                            # indexing and Sliding always start from 0 position 
# Ind = My_name[5]

# print(Ind)


# Slicing(accessing parts of String ) ---------------------------------

# My_name = "sailesh Aryal"

# print(My_name[3:7])              #this will print from 3 - 7 
# print(My_name[:4])              # this will print form 0 to 4
# print(My_name[4:])              # this will print from 4  up to last


#----------------------More function on String-----------------------#

# str = "My name is sailesh"

# print(str.endswith("sh"))
# print(str.endswith("sa"))

# str = str.capitalize()

# print(str.capitalize)
# print(str)

# print(str.replace("s", "e"))
# print(str.find("m"))
# print(str.count("Sailesh"))
# print(str.upper())


# --------------------------- Write a program to input users's first name & print its lenth ----------------------#

User_name = input("Write down your name :")
name_len = len(User_name)

print( "The lenght of your name is ",name_len)



# -------------------------------- Write a program to find the occurance of $ in a string -----------------------#

Str = " hi & sailesh & how are you. $ i am fine here"
print("the occuracne of $ is, ",Str.count("&"))






