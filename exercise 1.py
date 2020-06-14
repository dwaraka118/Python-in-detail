name = input("enter your name : ")
# print(f"your capitalized name is {name.capitalize()}")
print(f"your capitalized name is {name[0].upper()+name[1:]}")
print(name.upper())


file_name = input("what file would you like to open ? : ")
with open(file_name,'r') as file_object:
    print(file_object.read())
    m = file_object.read()
    print(m.capitalize())


import random
list1 = [1,2,3,4,5]
print(random.choice(list1))


from datetime import datetime as dt 
today = dt.now() 
print(today)
date_string = dt.strftime(today, '%m/%d/%Y') 
print(date_string)