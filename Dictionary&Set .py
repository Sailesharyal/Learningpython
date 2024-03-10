# intro = {
#     "Name" : "Apna collage",
#     "Age" : 45 , 
#     "Address" : ["Boudha","Jorpati"],
#     "Language" : ("C+","Pyhton","JAVA"),

# }

# print(intro)


# intro["Name"] =  "sailesh Aryal" # overwrite 
# intro["location"] = "Besigaun" # adding more key 

# print(intro)


# --------------------null Dictionary ------------------------------#

# Null_Dectionary = {}
# Null_Dectionary["name"] = "Bihan Pandey"
# Null_Dectionary["Class"] = "Five"
# print(Null_Dectionary)


# ----------------------- Nested Dictionary ----------------------------#

# Detail = {
#     "Name" : "Sailesh",
#     "age" : "Twenty",
#     "location" : {
#         1 : "Boudha",
#         2 :  "Besigaun",
#         3 : "Jorpati" 
#     },
#     "Hi" : "Hello"
# }

# print(Detail)
# print(Detail["location"]) # print a=only one key 




# # --------------------methods of Dictionary -------------------------------#

# intro = {
#     "Name" : "Sailesh Aryal",
#     "Age" : 45 , 
#     "Address" : ["Boudha","Jorpati"],
#     "Language" : ("C+","Pyhton","JAVA"),

# }



# # print(intro.keys())
# # print(len(list(intro.keys())))    #converting into list 


# # #---Value method-----#
# # print(intro.values())      #returning all value 


# #---items method------#      

# print(intro.items())

# pairs =list(intro.items())
# print(pairs[1])   # printng the iteam with indexing 


# # ------Get method -----------# 


# print(intro["Name"])                    # these two are the same function but use case a different while using a get method we don't get error(none value )but we get user using a normal funcation 
# print(intro.get("Name"))                # if the values are not there 


# # ---------------Update  method---------------------#
# intro.update({"age": "Twenty"})
# print(intro)