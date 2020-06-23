# declaration of dictionary
d = {'Dwaraka':24,'kishore':29,'haripriya':25,'lalith':23} 

# declaring empty list
d1 = []
d2 = []

# name = key age = value both together called item
for name,age in d.items(): 
    d1.append(name) # Appending keys to the list
    d2.append(age) # Appending valules to the list
    print(f'hi {name} you are {age} years old') # using Keys and values

print('this is d : ',d) # printing dictionary
print(f'this is d1 : {list(d1)} \nthis is d2 : {list(d2)}') # printing  keys and values in the form of list 
