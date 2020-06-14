number = int(input('enter the number of * you wanted : ' ))
for i in range(number+1):
    print(i * '*')

for i in range(number+1):
    i = i * " *"  # with small variation
    print(i)

for i in range(number+1):
    if i > 3:
        print(i)

