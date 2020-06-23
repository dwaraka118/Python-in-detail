'''
list comprihensions

l1= [n*6 for n in range(1,11)]
print(l1)'''


# normal loop

l1 = []
for i in range(1,11):
    l1.append(i*6)

print(l1)

# only even multiples
l1 = []
for i in range(1,11):
    if i % 2 == 0 :
        l1.append(i*6)

print(l1)