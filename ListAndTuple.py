"""
# # # --------------List is used to store multiple data item in a single varibale 

ThisIsList = ["apple" , "Car", "Cherry"]
print(ThisIsList)

# # # ---------------in list we can add Multipal Data type 
ThisIsList2 = ["apple", 12 , 13.80, "Boudha"]
print(ThisIsList2)
print(ThisIsList2[1])

# #--------------- # the biggest Difference between String and list is that the string is immutable(can't be change) but List(Can be cahnge) or Mutable
str = "Sailesh"
print(str[0])
ThisIsList[0] ="Sailesh"
print(ThisIsList)


# #----------------Slicing in List ----------------------#

Lis1 = ["Karan",19, 40, "Aryal"]
print(Lis1[:3])   #Slicing From beggining to index 3
print(Lis1[0:])    # sicing from 0 index to last
print(Lis1[0:2])  # slicing form 0 index to 2



#----------------------------Some methods in  list ----------------------------# 

My_list = ["sailesh", "Aryal", 21 , 2059]
print(My_list)

# # Append method(To add any data in last of list)

My_list.append("Sailesh")
print(My_list)
print(len(My_list))   # mutate the list this is called 


# # Sorting Method 
My_list = [7,2,9,10,55]
My_list.sort()          #Sorted the List
My_list.append(4)          # added 4 at last 
My_list.sort()              # again sorted the value 
print(My_list)


# # Reverse Sorting Method 

My_list.sort(reverse=True)   # Sorted in Decending order 
print(My_list)\


My_list = ["Apple", "zanana", "Car"]   
My_list.sort()   # USing Sorting method in String List
print(My_list)

#-----------------------Reversing method-----------#

My_list.reverse()
print(My_list)


#----------------------------Insert Mwthod-------------------------# 

My_list.insert(2 , 111)
print(My_list)


#--------------------Remove Method ------------------#
My_list.remove(10)
print(My_list)


#---------------Pop Method---------------#

My_list.pop(2)
print(My_list)

"""

"""

# Tupple(Tupple is immutable )

tup = (1,2,3,4,3,5,7,4,4)

print(tup)
print(len(tup))
print(type(tup))


# Slicing in Tuple

print(tup[0:2])

print(tup[:3])

print(tup[1::2])


#Indexing and Count Mehtods in tuple 

print(tup.index(3))            # this method is used to know the index of the particular data 

print(tup.count(4))   # this method is used to  count a particular data

"""



# Ask the user for the theree movie watch bt them and store them in a list 

movie = []

# # mov1 = input("Write name of movie")
# # mov2 = input("Write the name of second movie")
# # mov3 = input("Wrtie the name of third movie")


# # movie.append(mov1)
# # movie.append(mov2)
# # movie.append(mov3)

# print(movie)




mov = input("Put down any name of movie")
movie.append(mov)
mov = input("Put down the name of movie")
movie.append(mov)
mov = input("Write down the name of movie")
movie.append(mov)

print(movie)

























